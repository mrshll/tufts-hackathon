# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, make_response, render_template, flash, redirect, url_for, session, escape, g
from models.database import db_session
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('app.cfg')

# Instantiate DB
db = SQLAlchemy(app)
from models.appmodels import *

## Set SQL Alchemy to automatically tear down
@app.teardown_request
def shutdown_session(exception=None):
  db_session.remove()

def index():
  return render_template('index.html')

def sponsors():
  return render_template('sponsors.html')

def idea():
  if request.method == 'POST':
    name  = request.form['name']
    email = request.form['email']
    idea  = request.form['idea']
    idea = Idea(name=name, email=email, idea=idea)

    db.session.add(idea)
    db.session.commit()
    return redirect(url_for('idea'))
  elif request.method == 'GET':
    ideas = Idea.query.all()
    return render_template('idea.html', ideas=ideas, index=range(len(ideas)))
  else:
    return render_template('index.html')

idea.methods=['GET', 'POST']

# URLs
app.add_url_rule('/', 'index', index)
app.add_url_rule('/idea/', 'idea', idea)

if __name__ == "__main__":
  try:
    open('/tmp/app.db')
  except IOError:
    db.create_all()
  app.run(debug=True,host='127.0.0.1')
