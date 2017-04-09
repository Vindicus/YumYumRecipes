YumYum Recipes
===================

**YumYum** is a website where all professional and/or home chefs can share their recipes with the world.

----------


###TABLE OF CONTENTS
-------------

1. Requirements
2. Quick Start Guide
3. How To Use

#### REQUIREMENTS

The requirement to launch this application is:
1. A Facebook developer account for creating a recipe on YumYum at <a href="developers.facebook.com">Facebook developer</a>
2. Additionally, add your url domain such as localhost in your dashboard settings to authorize the domain to access Facebook API.
3. You will need a client ID and a client secret. Add them to fbclient_secrets.json file.
4. Install the necessary modules: sqlalchemy, oauth2client, flask.
4. This website uses <a href="https://www.sqlite.org/">Sqlite3</a> database and <a href="https://www.python.org/">Python</a>
5. You can launch this application on your local/virtual machine or through an online IDE such as <a href="https://c9.io/">Cloud9</a>
6. Once application is launched, login and application will take you via Facebook API to access.


#### QUICK START GUIDE

1. In the main.py file, determine if you are planning to launch this application via Cloud9 or a local/virtual machine. (If you plan to run on Cloud9, uncomment the lines 369-372)
2. Run the files yumyum_database_setup.py which creates the database and query_test.py which creates test data for the application.
3. In fbclient_secrets.json file, insert your client ID and client secret

#### HOW TO USE

1. Open your browser and access your domain such as localhost:5000.
2. Access the login page on the top right corner using the Facebook API.
3. Once logged in, you can create a new recipe, edit a recipe, or delete a recipe.