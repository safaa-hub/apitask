from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref
from sqlalchemy import create_engine
from myproject.myapp.models import User


engine = create_engine("mysql+pymysql://root:Root@localhost/django", echo=True)
engine.connect()

session = scoped_session(sessionmaker(bind=engine))
s = session()


#  print(engine)
def create_user(User):
    s.add(User)
    s.commit()
    s.close()


def is_valid(user_name, password):
    user = s.query(User).filter_by(user_name=user_name, password=password)
    if user is not None:
        return True
    else:
        return False


def get_user(id):
    user = s.query(User).filter_by(id=id)
    return user
