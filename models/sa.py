"""
Module to provide plug-and-play authentication support for SQLAlchemy.
"""

import datetime
from sqlalchemy import Column, Integer, String, DateTime
from flaskext.auth import AuthUser, get_current_user_data

def get_idea_class(declarative_base):
  class Idea(declarative_base):
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
        'id': self.id
        'name': self.name,
        'email': self.email,
        'idea': self.idea,
      }
  return Idea


