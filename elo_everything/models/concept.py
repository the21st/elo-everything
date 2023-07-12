from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Concept(Base):
    __tablename__ = 'concepts'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    image_url = Column(String)
    elo_score = Column(Float, default=1200)

    def __init__(self, name, image_url):
        self.name = name
        self.image_url = image_url

    def __repr__(self):
        return f"<Concept(name={self.name}, elo_score={self.elo_score})>"