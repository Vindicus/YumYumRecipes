#  import flask framework
from flask import Flask, render_template, request, redirect, \
                  jsonify, url_for, flash
from flask import make_response

#  import sqlalchemy for database connection
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker, exc
from yumyum_database_setup import Base, RecipeCategory, Recipe, User

# antiforgery session tokens client-server communication
from flask import session as login_session
from functools import wraps

import os
import time
import random
import string
import httplib2
import json
import requests
import random
import string

# import OAuth2Client
# for user authentications
from oauth2client.client import flow_from_clientsecrets, \
                                FlowExchangeError, AccessTokenCredentials

# connect to Dabase and create session
engine = create_engine('sqlite:///yumyumrecipes.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)

# decorator for checking if user is logged in
def login_required(f):
    @wraps(f)
    def login(*args, **kwargs):
        if 'username' not in login_session:
            return redirect(url_for('showLogin', next=request.url))
        return f(*args, **kwargs)
    return login


# user login
@app.route('/login/')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase +
                    string.digits) for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


#  connects to facebook API
@app.route('/auth/fbconnect', methods=['POST'])
def fbconnect():
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = request.data
    app_id = json.loads(open('fbclient_secrets.json',
                        'r').read())['web']['app_id']
    app_secret = json.loads(open('fbclient_secrets.json',
                            'r').read())['web']['app_secret']
    url = 'https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=%s&client_secret=%s&fb_exchange_token=%s' % (app_id, app_secret, access_token)  # noqa
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    # Use token to get user info from API
    userinfo_url = "https://graph.facebook.com/v2.4/me"
    # strip expire tag from access token
    token = result.split("&")[0]
    url = 'https://graph.facebook.com/v2.4/me?%s&fields=name,id,email' % token  # noqa
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    data = json.loads(result)
    # store info into session
    login_session['provider'] = 'facebook'
    login_session['username'] = data["name"]
    login_session['email'] = data["email"]
    login_session['facebook_id'] = data["id"]
    stored_token = token.split('=')[1]
    login_session['access_token'] = stored_token
    url = 'https://graph.facebook.com/v2.4/me/picture?%s&redirect=0&height=200&width=200' % token  # noqa
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    data = json.loads(result)
    login_session['picture'] = data['data']['url']

    # check if user exists
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
        login_session['user_id'] = user_id
    flash("Welcome %s" % login_session['username'])
    return login_session['username']


# checks if the user is in our database
def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


# adds user to our database
def createUser(login_session):
    newUser = User(name=login_session['username'],
                   email=login_session['email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


# logs the user out
@app.route('/logout/')
def logout():
    return redirect(url_for('fbdisconnect'))


# disconnect from facebook API
@app.route('/fbdisconnect')
def fbdisconnect():
    if login_session:
        facebook_id = login_session['facebook_id']
        # The access token must me included to successfully logout
        access_token = login_session['access_token']
    else:
        return redirect(url_for('listRecipes'))
    url = 'https://graph.facebook.com/%s/permissions?access_token=%s' % (facebook_id, access_token)  # noqa
    h = httplib2.Http()
    result = h.request(url, 'DELETE')[1]
    for key in login_session.keys():
        del login_session[key]
    return redirect(url_for('listRecipes'))


#  homepage that lists the most recipes by category
@app.route('/')
def listRecipes():
    recipes = session.query(RecipeCategory.name.label("category"),
                            Recipe.name.label("recipe"),
                            Recipe.description,
                            Recipe.ingredients,
                            Recipe.instructions,
                            Recipe.user_id). \
                            outerjoin(Recipe,
                                      RecipeCategory.id ==
                                      Recipe.recipe_category_id).order_by(
                                      desc(Recipe.date)).all()
    return render_template('showRecipes.html', recipes=recipes, login_session=login_session)


#  lists the recipes in the selected category
@app.route('/<category_name>/')
def showCategory(category_name):
    try:
        category = session.query(
                                 RecipeCategory
                                 ).filter_by(
                                             name=category_name
                                             ).one()
        recipes = session.query(
                                Recipe
                                ).filter_by(
                                            recipe_category_id=category.id
                                            ).all()
        return render_template('category.html',
                               category=category, recipes=recipes, login_session=login_session)
    except exc.NoResultFound as e:
        return "Unable to find category"


#  creates a new recipe
@app.route('/recipe/new/', methods=['GET', 'POST'])
@login_required
def newRecipe():
    # determines if the user is authenticated to access this page
    # for both GET and POST method
        if request.method == 'POST':
            name = request.form['name']
            description = request.form['description']
            ingredients = request.form['ingredients']
            instructions = request.form['instructions']
            category = request.form['category']
            if name == "" or \
               description == "" or ingredients == "" or \
               instructions == "" or category == 0:
                flash("Please complete all fields")
                return redirect(url_for('newRecipe'))
            else:
                try:
                    category_one = session.query(
                                                 RecipeCategory
                                                 ).filter_by(
                                                             id=category
                                                             ).one()
                    newRecipe = Recipe(
                                       name=name,
                                       description=description,
                                       ingredients=ingredients,
                                       instructions=instructions,
                                       recipe_category_id=category,
                                       user_id=getUserID(login_session['email']))
                    session.add(newRecipe)
                    flash("Recipe created!")
                    session.commit()
                    return redirect(url_for('showRecipe',
                                            category_name=category_one.name,
                                            recipe_id=newRecipe.id))
                except exc.NoResultFound as e:
                    flash("Error in creating recipe. Please try again")
                    return redirect(url_for('newRecipe'))
        else:
            recipe_category = session.query(RecipeCategory).all()
            return render_template('newrecipe.html',
                                   recipe_category=recipe_category, login_session=login_session)


# refactoring to place code here to determine
# if category exists in the database based on the URL
# otherwise return False
def category_q(category_name, recipe_id):
    try:
        recipe = session.query(Recipe).filter_by(id=recipe_id).one()
        if recipe.recipe_category.name == category_name:
            return recipe
        else:
            return False
    except exc.NoResultFound as e:
        return False


# lists the recipe information
@app.route('/<category_name>/<int:recipe_id>/')
def showRecipe(category_name, recipe_id):
    result = category_q(category_name, recipe_id)
    if result:
        return render_template('recipe.html', recipe=result, login_session=login_session)
    else:
        return "Failed to find what your looking for"


#  allow users to edit their recipes
@app.route('/<category_name>/<int:recipe_id>/edit/', methods=['GET', 'POST'])
@login_required
def editRecipe(category_name, recipe_id):
        try:
            recipe_auth = session.query(Recipe).filter_by(id=recipe_id).one()
        except exc.NoResultFound as e:
            return "Unable to find recipe"
        if login_session['email'] != recipe_auth.user.email:
            flash("You are not authorized to edit this post")
            return redirect(url_for('showCategory',
                                    category_name=category_name))
        else:
            if request.method == 'POST':
                editName = request.form['name']
                editDescription = request.form['description']
                editIngredients = request.form['ingredients']
                editInstructions = request.form['instructions']
                editCategory = request.form['category']
                if editName == "" or editDescription == "" or \
                   editIngredients == "" or editInstructions == "" or \
                   editCategory == "0":
                    flash("Please complete all fields")
                    return redirect(url_for('editRecipe',
                                            category_name=category_name,
                                            recipe_id=recipe_id))
                else:
                    try:
                        category = session.query(
                                                 RecipeCategory
                                                 ).filter_by(
                                                             id=editCategory
                                                             ).one()
                        recipe = session.query(
                                               Recipe
                                               ).filter_by(
                                                           id=recipe_id
                                                           ).one()
                        recipe.name = editName
                        recipe.description = editDescription
                        recipe.ingredients = editIngredients
                        recipe.instructions = editInstructions
                        recipe.recipe_category_id = category.id
                        session.add(recipe)
                        flash("Updated Successfully!")
                        session.commit()
                        return redirect(url_for('showRecipe',
                                                category_name=recipe.
                                                recipe_category.name,
                                                recipe_id=recipe.id))
                    except exc.NoResultFound as e:
                        flash("Update Error, please try again")
                        return redirect(url_for('editRecipe',
                                                category_name=category_name,
                                                recipe_id=recipe_id))
            else:
                result = category_q(category_name, recipe_id)
                if result:
                    recipe_category = session.query(RecipeCategory).all()
                    return render_template('editrecipe.html',
                                           recipe=result,
                                           recipe_category=recipe_category,
                                           login_session=login_session)
                else:
                    return "Unable to find what your looking for"


# deletes the recipe for authorized users only
@app.route('/<category_name>/<int:recipe_id>/delete/')
@login_required
def deleteRecipe(category_name, recipe_id):
        try:
            recipe_auth = session.query(Recipe).filter_by(id=recipe_id).one()
        except exc.NoResultFound as e:
            return "Unable to find recipe"
        if login_session['email'] != recipe_auth.user.email:
            flash("You are not authorized to delete this post")
            return redirect(url_for('showCategory',
                                    category_name=category_name))
        else:
            result = category_q(category_name, recipe_id)
            if result:
                session.delete(recipe_auth)
                flash("Recipe Deleted!")
                session.commit()
                return redirect(url_for('showCategory',
                                        category_name=category_name))
            else:
                return "Unable to find what your looking for"


# JSON APIs to view category Information
@app.route('/<category_name>/JSON/')
def categoryJSON(category_name):
    try:
        category = session.query(
                                 RecipeCategory
                                 ).filter_by(
                                             name=category_name
                                             ).one()
        if category.name == category_name:
            recipes = session.query(
                                    Recipe
                                    ).filter_by(
                                                recipe_category_id=category.id
                                                ).all()
            return jsonify(Recipe=[i.serialize for i in recipes])
    except exc.NoResultFound as e:
        return "Cannot jsonify"


# JSON APIs to view specific recipe Information
@app.route('/<category_name>/<int:recipe_id>/JSON/')
def recipeJSON(category_name, recipe_id):
    result = category_q(category_name, recipe_id)
    if result:
        recipe = session.query(Recipe).filter_by(id=recipe_id).one()
        return jsonify(Recipe=recipe.serialize)
    else:
        return "Unable to jsonify"

# Use this if your running web server on cloud9
# if __name__ == '__main__':
#    app.secret_key = 'super_secret_key'
#    app.debug = True
#    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))

# Use this if running on local/virtual machine
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
