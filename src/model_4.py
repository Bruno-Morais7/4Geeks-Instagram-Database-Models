import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(25), nullable=False)
    firstname = Column(String(20), nullable=False)
    lastname = Column(String(20), nullable=False)
    email = Column(String(100), nullable=False)

class Album(Base):
    __tablename__ = 'album'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(String(200))
    user_id = Column(Integer, ForeignKey('user.id'), unique=True)
    user = relationship(User)

class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    position = Column(String(200))


class Photo(Base):
    __tablename__ = 'photo'
    id = Column(Integer, primary_key=True)
    title = Column (String(120))
    description = Column (String(250))
    image_path = Column (String(50))
    user_id = Column(Integer, ForeignKey('user.id'), unique=True)
    album_id = Column(Integer, ForeignKey('album.id'))
    location_id = Column(Integer, ForeignKey('location.id'))
    user = relationship("User")


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    date = Column (String(20))
    content = Column(String(500))
    photo_id = Column(Integer, ForeignKey('photo.id'))
    photo = relationship(Photo)

class Likes(Base):
    __tablename__ = 'post_likes'
    id = Column(Integer, primary_key=True)
    likes = Column(Integer)
    photo_id = Column(Integer, ForeignKey('photo.id'))
    photo = relationship(Photo)


class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer)
    user = relationship(User)


    def to_dict(self):
        return {}

try:
    result = render_er(Base, 'diagram_4.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e