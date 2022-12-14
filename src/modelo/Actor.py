from sqlalchemy import Column, Integer,String, Date
from sqlalchemy.orm import relationship
from src.modelo.declarative_base import Base
from src.modelo.Movie import Movie


class Actor(Base):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    birthday = Column(Date)

    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday