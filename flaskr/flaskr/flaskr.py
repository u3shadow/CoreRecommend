# -*- coding=UTF-8 -*-
import os
import random
import uuid
import json
import psycopg2 as psy
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from basecontent.MainToFlask import calculate

import sys
sys.path.append('../')
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
    rv = psy.connect(database="redb", user="u3", password=" ")
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
    cursor = db.cursor(cursorclass=psy.cursors.DictCursor)
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
    db = get_db()
    cursor = db.cursor()
    if request.method == 'POST':
        cursor.execute('select count(*) from users where name=\'%s\' and psw=\'%s\''%(request.form['name'],request.form['psw']))
        sum = cursor.fetchall()[0][0]
        if sum == 0:
            code = 230
            userid = -1;
        else:
            cursor.execute('select userid from users where name=\'%s\' and psw=\'%s\''%(request.form['name'],request.form['psw']))
            userid = cursor.fetchall()[0][0]
            session['logged_in'] = True
            flash('You were logged in')
            code = 200
        dic = {'code':code,'userid':userid}
        response = app.response_class(
            response=json.dumps(dic),
            status=200,
            mimetype='application/json')
        return response
    else:
        dic = {'code':231}
        response = app.response_class(
            response=json.dumps(dic),
            status=400,
            mimetype='application/json')
        return response
@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        name1 = request.form['name']
        psw = request.form['psw']
        email = request.form['email']
        db = get_db()
        cursor = db.cursor()
        cursor.execute('select COUNT(name) from users where name=\'%s\''%name1)
        sumname = (cursor.fetchall())[0][0]
        cursor.execute('select COUNT(email) from users where email=\'%s\''%email)
        sumemail = (cursor.fetchall())[0][0]
        print sumname
        print sumemail
        code = 200
        if sumname > 0:
            code = 230
        if sumemail > 0:
            code = 231
        if code == 200:
            cursor.execute('insert into users (name,psw,email,userid) values (%s,%s,%s,%s)',
                 [name1,psw,email,str(uuid.uuid4())])
            db.commit()
        dic = {'code':code}
        response = app.response_class(
            response=json.dumps(dic),
            status=200,
            mimetype='application/json')
        return response
@app.route('/calrate',methods = ['POST'])
def calrate():
    if request.method =='POST':
        rate = request.form['rates']
        userid = request.form['id']
        dic = eval(rate)
        calculate(dic)
        response = app.response_class(
            status=200,
            mimetype='application/json')
        return response
@app.route('/getgames',methods = ['POST'])
def getgames():
    if request.method =='POST':
        db = connect_db()
        userid = request.form['id']
        cur = db.cursor()
        cur.execute("select count(*) from games;")
        numgame = cur.fetchall()[0][0]
        ran = range(numgame)
        li = random.sample(ran, 10)
        idList = []
        for i in range(1, 11):
            cur.execute('select steamid from games where id=\'%s\';'%i)
            gameid = cur.fetchall()[0][0]
            print gameid
            idList.append(gameid)
        response = app.response_class(
            response = json.dumps(idList),
            status=200,
            mimetype='application/json')
        return response
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))