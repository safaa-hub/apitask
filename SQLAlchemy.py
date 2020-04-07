from django.db import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref
from sqlalchemy import create_engine
from myproject.myapp.models import User

engine = create_engine("mysql+pymysql://root:Root@localhost/django", echo=True)
engine.connect()


#  print(engine)
def create_user(User):
    session = scoped_session(sessionmaker(bind=engine))
    s = session()
    s.add(User)
    s.close()
