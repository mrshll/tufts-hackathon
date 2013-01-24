# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, make_response, render_template, flash, redirect, url_for, session, escape, g
from models.database import db_session
from flask.ext.sqlalchemy import SQLAlchemy
from random import shuffle
import os

app = Flask(__name__)
app.config.from_pyfile('app.cfg')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

# Instantiate DB
db = SQLAlchemy(app)
from models.appmodels import *

## Set SQL Alchemy to automatically tear down
@app.teardown_request
def shutdown_session(exception=None):
  db_session.remove()

def index():
  return render_template('index.html', page_name="index")

def resources():
  return render_template('resources.html', page_name="resources")

def idea():
  if request.method == 'POST':
    name  = request.form['name']
    email = request.form['email']
    idea  = request.form['idea']
    idea = Idea(name=name, email=email, idea=idea)

    db.session.add(idea)
    try:
      db.session.commit()
      return redirect(url_for('idea'))
    except:
      db.session.rollback()
      flash("Coundn't save your idea :( One of the fields was probably" \
            "too long (name < 80 characters, email < 50, idea < 200)")
      return redirect(url_for('idea'))
  elif request.method == 'GET':
    ideas = Idea.query.all()
    shuffle(ideas)
    return render_template('idea.html', page_name="idea", ideas=ideas, index=range(len(ideas)))
  else:
    return render_template('index.html')

idea.methods=['GET', 'POST']

# URLs
app.add_url_rule('/', 'index', index)
app.add_url_rule('/idea/', 'idea', idea)
app.add_url_rule('/resources/', 'resources', resources)


if __name__ == "__main__":
  try:
    open('/tmp/app.db')
  except IOError:
    db.create_all()
  app.run(port=os.environ['PORT'])
