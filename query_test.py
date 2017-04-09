#  import sqlalchemy for database connection
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker, exc
from yumyum_database_setup import Base, RecipeCategory, Recipe, User

# connect to Dabase and create session
engine = create_engine('sqlite:///yumyumrecipes.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# RecipeCategory list
indian = RecipeCategory(name="Indian Cuisine")
session.add(indian)
western = RecipeCategory(name="Western Cuisine")
session.add(western)
asian = RecipeCategory(name="Asian Cuisine")
session.add(asian)
dessert = RecipeCategory(name="Desserts")
session.add(dessert)
fruit=RecipeCategory(name="Fruit Craft")
session.add(fruit)
appetizer=RecipeCategory(name="Appetizers")
session.add(appetizer)
vegetarian=RecipeCategory(name="Vegetarian")
session.add(vegetarian)
bakery=RecipeCategory(name="Bakery")
session.add(bakery)
italian=RecipeCategory(name="Italian Cuisine")
session.add(italian)
#session.commit()

# Recipes list
# Asian Cusine test data
gyoza = Recipe(name="Gyoza",
               description="They're great hot or cold, and may be eaten plain or with the dipping sauce.",
               ingredients="sesame oil, cabbage, chopped onion, garlic, carrot, ground pork.",
               instructions="Heat sesame oil in a large skillet over medium high heat. Mix in cabbage, onion, garlic and carrot.",
               recipe_category_id=3,
               user_id=2)

session.add(gyoza)

eggroll = Recipe(name="Egg Roll",
                 description="hot and crunchy",
                 ingredients="vegetable, sesame oil",
                 instructions="fry and eat",
                 recipe_category_id=3,
                 user_id=2)
session.add(eggroll)

sushi = Recipe(name="Sushi",
               description="They're great hot or cold, and may be eaten plain or with the dipping sauce.",
               ingredients="sesame oil, cabbage, chopped onion, garlic, carrot, ground pork.",
               instructions="Heat sesame oil in a large skillet over medium high heat. Mix in cabbage, onion, garlic and carrot.",
               recipe_category_id=3,
               user_id=2)

session.add(sushi)

tsochicken = Recipe(name="General Tso Chicken",
                 description="hot and good",
                 ingredients="chicken breast",
                 instructions="cook and eat",
                 recipe_category_id=3,
                 user_id=2)
session.add(tsochicken)

# Indian Cuisine test data
gyoza1 = Recipe(name="Gyoza",
               description="They're great hot or cold, and may be eaten plain or with the dipping sauce.",
               ingredients="sesame oil, cabbage, chopped onion, garlic, carrot, ground pork.",
               instructions="Heat sesame oil in a large skillet over medium high heat. Mix in cabbage, onion, garlic and carrot.",
               recipe_category_id=1,
               user_id=2)

session.add(gyoza1)

eggroll1 = Recipe(name="Egg Roll",
                 description="hot and crunchy",
                 ingredients="vegetable, sesame oil",
                 instructions="fry and eat",
                 recipe_category_id=1,
                 user_id=2)
session.add(eggroll1)
sushi1 = Recipe(name="Sushi",
               description="They're great hot or cold, and may be eaten plain or with the dipping sauce.",
               ingredients="sesame oil, cabbage, chopped onion, garlic, carrot, ground pork.",
               instructions="Heat sesame oil in a large skillet over medium high heat. Mix in cabbage, onion, garlic and carrot.",
               recipe_category_id=1,
               user_id=2)

session.add(sushi1)

tsochicken1 = Recipe(name="General Tso Chicken",
                 description="hot and good",
                 ingredients="chicken breast",
                 instructions="cook and eat",
                 recipe_category_id=1,
                 user_id=2)
session.add(tsochicken1)

# Western Cuisine test data
gyoza2 = Recipe(name="Gyoza",
               description="They're great hot or cold, and may be eaten plain or with the dipping sauce.",
               ingredients="sesame oil, cabbage, chopped onion, garlic, carrot, ground pork.",
               instructions="Heat sesame oil in a large skillet over medium high heat. Mix in cabbage, onion, garlic and carrot.",
               recipe_category_id=2,
               user_id=2)

session.add(gyoza2)

eggroll2 = Recipe(name="Egg Roll",
                 description="hot and crunchy",
                 ingredients="vegetable, sesame oil",
                 instructions="fry and eat",
                 recipe_category_id=2,
                 user_id=2)
session.add(eggroll2)
sushi2 = Recipe(name="Sushi",
               description="They're great hot or cold, and may be eaten plain or with the dipping sauce.",
               ingredients="sesame oil, cabbage, chopped onion, garlic, carrot, ground pork.",
               instructions="Heat sesame oil in a large skillet over medium high heat. Mix in cabbage, onion, garlic and carrot.",
               recipe_category_id=2,
               user_id=2)

session.add(sushi2)

tsochicken2 = Recipe(name="General Tso Chicken",
                 description="hot and good",
                 ingredients="chicken breast",
                 instructions="cook and eat",
                 recipe_category_id=2,
                 user_id=2)
session.add(tsochicken2)

# Desserts
gyoza4 = Recipe(name="Gyoza",
               description="They're great hot or cold, and may be eaten plain or with the dipping sauce.",
               ingredients="sesame oil, cabbage, chopped onion, garlic, carrot, ground pork.",
               instructions="Heat sesame oil in a large skillet over medium high heat. Mix in cabbage, onion, garlic and carrot.",
               recipe_category_id=4,
               user_id=2)

session.add(gyoza4)

eggroll4 = Recipe(name="Egg Roll",
                 description="hot and crunchy",
                 ingredients="vegetable, sesame oil",
                 instructions="fry and eat",
                 recipe_category_id=4,
                 user_id=2)
session.add(eggroll4)
sushi4 = Recipe(name="Sushi",
               description="They're great hot or cold, and may be eaten plain or with the dipping sauce.",
               ingredients="sesame oil, cabbage, chopped onion, garlic, carrot, ground pork.",
               instructions="Heat sesame oil in a large skillet over medium high heat. Mix in cabbage, onion, garlic and carrot.",
               recipe_category_id=4,
               user_id=2)

session.add(sushi4)

tsochicken4 = Recipe(name="General Tso Chicken",
                 description="hot and good",
                 ingredients="chicken breast",
                 instructions="cook and eat",
                 recipe_category_id=4,
                 user_id=2)
session.add(tsochicken4)

#Fruit Craft test data
gyoza5 = Recipe(name="Gyoza",
               description="They're great hot or cold, and may be eaten plain or with the dipping sauce.",
               ingredients="sesame oil, cabbage, chopped onion, garlic, carrot, ground pork.",
               instructions="Heat sesame oil in a large skillet over medium high heat. Mix in cabbage, onion, garlic and carrot.",
               recipe_category_id=5,
               user_id=2)

session.add(gyoza5)

eggroll5 = Recipe(name="Egg Roll",
                 description="hot and crunchy",
                 ingredients="vegetable, sesame oil",
                 instructions="fry and eat",
                 recipe_category_id=5,
                 user_id=2)
session.add(eggroll5)
sushi5 = Recipe(name="Sushi",
               description="They're great hot or cold, and may be eaten plain or with the dipping sauce.",
               ingredients="sesame oil, cabbage, chopped onion, garlic, carrot, ground pork.",
               instructions="Heat sesame oil in a large skillet over medium high heat. Mix in cabbage, onion, garlic and carrot.",
               recipe_category_id=5,
               user_id=2)

session.add(sushi5)

tsochicken5 = Recipe(name="General Tso Chicken",
                 description="hot and good",
                 ingredients="chicken breast",
                 instructions="cook and eat",
                 recipe_category_id=5,
                 user_id=2)
session.add(tsochicken5)

#Appetizers test data
gyoza6 = Recipe(name="Gyoza",
               description="They're great hot or cold, and may be eaten plain or with the dipping sauce.",
               ingredients="sesame oil, cabbage, chopped onion, garlic, carrot, ground pork.",
               instructions="Heat sesame oil in a large skillet over medium high heat. Mix in cabbage, onion, garlic and carrot.",
               recipe_category_id=6,
               user_id=2)

session.add(gyoza6)

eggroll6 = Recipe(name="Egg Roll",
                 description="hot and crunchy",
                 ingredients="vegetable, sesame oil",
                 instructions="fry and eat",
                 recipe_category_id=6,
                 user_id=2)
session.add(eggroll6)
sushi6 = Recipe(name="Sushi",
               description="They're great hot or cold, and may be eaten plain or with the dipping sauce.",
               ingredients="sesame oil, cabbage, chopped onion, garlic, carrot, ground pork.",
               instructions="Heat sesame oil in a large skillet over medium high heat. Mix in cabbage, onion, garlic and carrot.",
               recipe_category_id=6,
               user_id=2)

session.add(sushi6)

tsochicken6 = Recipe(name="General Tso Chicken",
                 description="hot and good",
                 ingredients="chicken breast",
                 instructions="cook and eat",
                 recipe_category_id=6,
                 user_id=2)
session.add(tsochicken6)

# Vegetarian test data
gyoza7 = Recipe(name="Gyoza",
               description="They're great hot or cold, and may be eaten plain or with the dipping sauce.",
               ingredients="sesame oil, cabbage, chopped onion, garlic, carrot, ground pork.",
               instructions="Heat sesame oil in a large skillet over medium high heat. Mix in cabbage, onion, garlic and carrot.",
               recipe_category_id=7,
               user_id=2)

session.add(gyoza7)

eggroll7 = Recipe(name="Egg Roll",
                 description="hot and crunchy",
                 ingredients="vegetable, sesame oil",
                 instructions="fry and eat",
                 recipe_category_id=7,
                 user_id=2)
session.add(eggroll7)
sushi7 = Recipe(name="Sushi",
               description="They're great hot or cold, and may be eaten plain or with the dipping sauce.",
               ingredients="sesame oil, cabbage, chopped onion, garlic, carrot, ground pork.",
               instructions="Heat sesame oil in a large skillet over medium high heat. Mix in cabbage, onion, garlic and carrot.",
               recipe_category_id=7,
               user_id=2)

session.add(sushi7)

tsochicken7 = Recipe(name="General Tso Chicken",
                 description="hot and good",
                 ingredients="chicken breast",
                 instructions="cook and eat",
                 recipe_category_id=7,
                 user_id=2)
session.add(tsochicken7)

# bakery test data
gyoza8 = Recipe(name="Gyoza",
               description="They're great hot or cold, and may be eaten plain or with the dipping sauce.",
               ingredients="sesame oil, cabbage, chopped onion, garlic, carrot, ground pork.",
               instructions="Heat sesame oil in a large skillet over medium high heat. Mix in cabbage, onion, garlic and carrot.",
               recipe_category_id=8,
               user_id=2)

session.add(gyoza8)

eggroll8 = Recipe(name="Egg Roll",
                 description="hot and crunchy",
                 ingredients="vegetable, sesame oil",
                 instructions="fry and eat",
                 recipe_category_id=8,
                 user_id=2)
session.add(eggroll8)
sushi8 = Recipe(name="Sushi",
               description="They're great hot or cold, and may be eaten plain or with the dipping sauce.",
               ingredients="sesame oil, cabbage, chopped onion, garlic, carrot, ground pork.",
               instructions="Heat sesame oil in a large skillet over medium high heat. Mix in cabbage, onion, garlic and carrot.",
               recipe_category_id=8,
               user_id=2)

session.add(sushi8)

tsochicken8 = Recipe(name="General Tso Chicken",
                 description="hot and good",
                 ingredients="chicken breast",
                 instructions="cook and eat",
                 recipe_category_id=8,
                 user_id=2)
session.add(tsochicken8)

#Italian Cuisine test data
gyoza9 = Recipe(name="Gyoza",
               description="They're great hot or cold, and may be eaten plain or with the dipping sauce.",
               ingredients="sesame oil, cabbage, chopped onion, garlic, carrot, ground pork.",
               instructions="Heat sesame oil in a large skillet over medium high heat. Mix in cabbage, onion, garlic and carrot.",
               recipe_category_id=9,
               user_id=2)

session.add(gyoza9)

eggroll9 = Recipe(name="Egg Roll",
                 description="hot and crunchy",
                 ingredients="vegetable, sesame oil",
                 instructions="fry and eat",
                 recipe_category_id=9,
                 user_id=2)
session.add(eggroll9)
sushi9 = Recipe(name="Sushi",
               description="They're great hot or cold, and may be eaten plain or with the dipping sauce.",
               ingredients="sesame oil, cabbage, chopped onion, garlic, carrot, ground pork.",
               instructions="Heat sesame oil in a large skillet over medium high heat. Mix in cabbage, onion, garlic and carrot.",
               recipe_category_id=9,
               user_id=2)

session.add(sushi9)

tsochicken9 = Recipe(name="General Tso Chicken",
                 description="hot and good",
                 ingredients="chicken breast",
                 instructions="cook and eat",
                 recipe_category_id=9,
                 user_id=2)
session.add(tsochicken9)

session.commit()