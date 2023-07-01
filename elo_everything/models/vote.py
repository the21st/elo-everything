from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Vote(Base):
    __tablename__ = 'votes'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    concept_id = Column(Integer, ForeignKey('concepts.id'))

    user = relationship("User", back_populates="votes")
    concept = relationship("Concept", back_populates="votes")