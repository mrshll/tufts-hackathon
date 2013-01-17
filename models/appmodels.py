from sqlalchemy import Column, Integer, String
from database import Base
import datetime
from app import db

class Idea(db.Model):
  id    = Column(Integer, primary_key=True)
  name  = Column(String(80), nullable=False)
  email = Column(String(50))
  idea  = Column(String(140))

  def __init__(self, *args, **kwargs):
    self.name  = kwargs.get('name')
    self.email = kwargs.get('email')
    self.idea  = kwargs.get('idea')

  def __getstate__(self):
    return {
      'id': self.id,
      'name': self.name,
      'email': self.email,
      'idea': self.idea,
    }
  def __repr__(self):
    return "IDEA by NAME"
