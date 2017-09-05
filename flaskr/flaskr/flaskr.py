# -*- coding=UTF-8 -*-
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
sys.path.append('/home/u3/app/CoreRecommend')
sys.path.append('/home/u3-linux/PycharmProjects/CoreRecommend')
import psycopg2 as psy
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

import sys
sys.path.append('../')
app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE = os.path.join(app.root_path,'flaskr'),
    SECRET_KEY = 'development key'
))
app.config.from_envvar('FLASKR_SETTINGS',silent=True)
def connect_db():
    """Connects to the specific database."""
    rv = psy.connect(database="redb", user="u3", password=" ")
    return rv
def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'PSQL'):
        g.PSQL = connect_db()
    return g.PSQL
@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'PSQL'):
        g.PSQL.close()
def init_db():
    return ""

@app.route('/')
def show_entries():
    return "<h1 style='color:blue'>Hello There!</h1>"



