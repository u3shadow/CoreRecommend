# -*- coding=UTF-8 -*-
import os
import MySQLdb as mysql
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE = os.path.join(app.root_path,'flaskr'),
    SECRET_KEY = 'development key',
    USERNAME = 'admin',
    PASSWORD = 'default'
))
app.config.from_envvar('FLASKR_SETTINGS',silent=True)
def connect_db():
    """Connects to the specific database."""
    rv = mysql.connect(host='localhost',user='root',passwd='u3shadow',db='test')
    return rv
def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'MySQLdb'):
        g.MySQLdb = connect_db()
    return g.MySQLdb
@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'MySQLdb'):
        g.MySQLdb.close()
def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().execute(f.read())
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')

@app.route('/')
def show_entries():
    db = get_db()
    cursor = db.cursor(cursorclass=mysql.cursors.DictCursor)
    cursor.execute('select title, text from entries order by id desc')
    entries = cursor.fetchall()
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.cursor().execute('insert into entries (title, text) values (%s, %s)',
                 [request.form['title'], request.form['text']])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))