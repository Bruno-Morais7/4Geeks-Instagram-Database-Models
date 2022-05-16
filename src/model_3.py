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
    user_feed = relationship("User_feed") #, back_populates="user", uselist=False)


class User_feed(Base):
    __tablename__ = 'user_feed'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), unique=True)
    post_id = Column(Integer, ForeignKey('posts.id'))
    #user = relationship("User", back_populates="user_feed", uselist=False)

    
class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(150))
    description = Column(String(500))
    user_feed_id = Column(Integer, ForeignKey('user_feed.id'))
    user_feed = relationship(User_feed)


class Post_comments(Base):
    __tablename__ = 'post_comments'
    id = Column(Integer, primary_key=True)
    comment = Column(String(500))
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship(Posts)

class Post_likes(Base):
    __tablename__ = 'post_likes'
    id = Column(Integer, primary_key=True)
    likes = Column(Integer)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship(Posts)


class User_followers(Base):
    __tablename__ = 'user_follower'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    follower_id = Column(Integer)
    user = relationship(User)


    def to_dict(self):
        return {}


try:
    result = render_er(Base, 'diagram_3.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e