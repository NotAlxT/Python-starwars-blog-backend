import os
import sys
import enum
from sqlalchemy import Integer, Enum
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Character(Base):
    __tablename__ = 'characters'
    name = Column(String(250), ForeignKey('vehicle.pilot'), ForeignKey('favorites.favorite_charaters'))
    planet_from = Column(String(250), ForeignKey('planets.name'))
    id = Column(Integer, primary_key=True)
    age = Column(Integer)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    size = Column(Integer)
    population = Column(Integer)
    climate = Column(String(250))
    name = Column(String(250), ForeignKey('favorites.favorite_planets'))

class Vehicle(Base):
    __tablename__="vehicle"
    id = Column(Integer, primary_key = True)
    name = Column(String(250), ForeignKey('favorites.favorite_vehicles'))
    pilot = Column(String(250))
    type = Column(String(250))

class User(Base):
     __tablename__ = 'user'
     id = Column(Integer, ForeignKey('favorites.user_id', primary_key=True))
     username = Column(String(250), nullable=False)
     firstname = Column(String(250), nullable=False)
     
class Favorites(Base):
    __tablename__= 'favorites'
    date_added = Column(DateTime(False))
    user_id = Column(Integer, primary_key=True)
    favorite_characters = Column(Integer, ForeignKey('characters.name'))
    favorite_planets = Column(Integer, ForeignKey('planets.name'))
    favorite_vehicles = Column(Integer, ForeignKey('vehicles.name'))

    def to_dict(self):
        return{}

render_er(Base, 'diagram.png')

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

# class User(Base):
#     __tablename__ = 'user'
#     id = Column(Integer, primary_key=True)
#     username = Column(String(250))
#     firstname = Column(String(250))
#     lastname = Column(String(250), nullable=False)
#     email = Column(String(250), unique=True)

# class Follower(Base):
#     __tablename__ = 'follower'
#     id = Column(Integer, primary_key=True)
#     user_from_id = Column(Integer, ForeignKey('user.id'))
#     user_to_id = Column(Integer, ForeignKey('user.id'))

# class Post(Base):
#     __tablename__ = 'post'
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('user.id'))  

# class MediaType(enum.Enum):
#     png = "png"
#     jpg = "jpg"
#     gif = "gif"

# class Media(Base):
#     __tablename__ = 'media'
#     id = Column(Integer, primary_key=True)
#     type = Column(Enum(MediaType))
#     url = Column(String(250))
#     post_id = Column(Integer, ForeignKey('post.id'))
    
# class Comment(Base):
#     __tablename__ = 'comment'
#     id = Column(Integer, primary_key=True)
#     comment_text = Column(String(250))
#     autor_id = Column(Integer, ForeignKey('user.id'))
#     post_id = Column(Integer, ForeignKey('post.id'))

#     def to_dict(self):
#         return {}

# ## Draw from SQLAlchemy base
# render_er(Base, 'diagram.png')




