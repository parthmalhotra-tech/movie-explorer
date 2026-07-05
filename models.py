from database import Base
from sqlalchemy import Column,Integer,String,ForeignKey
class User(Base):
    __tablename__="USER"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)


class Watchlist(Base):
    __tablename__ = "watchlist"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("USER.id"))
    imdb_id = Column(String, nullable=False)
    title = Column(String, nullable=False)
    poster = Column(String)
