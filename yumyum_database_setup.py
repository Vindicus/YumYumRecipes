#  sqlalchemy imports
from sqlalchemy import Column, ForeignKey, Integer, \
                       String, create_engine, Text, DateTime
from sqlalchemy import UniqueConstraint
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


#  stores user profile information from OAuth providers
class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


#  creates a table list of recipe categories
class RecipeCategory(Base):
    __tablename__ = "recipe_category"

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


# creates a list of recipes
class Recipe(Base):
    __tablename__ = "recipe"

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    description = Column(String(250), nullable=False)
    ingredients = Column(String(250))
    instructions = Column(Text)
    recipe_category_id = Column(Integer, ForeignKey('recipe_category.id'))
    recipe_category = relationship(RecipeCategory)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    date = Column(DateTime(timezone=True), server_default=func.now())

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'ingredients': self.ingredients,
            'instructions': self.instructions,
        }

engine = create_engine('sqlite:///yumyumrecipes.db')
Base.metadata.create_all(engine)
