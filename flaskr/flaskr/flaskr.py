# -*- coding=UTF-8 -*-
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
sys.path.append('/home/u3/CoreRecommend')
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
    if not hasattr(g, 'PSQL'):
        g.PSQL = connect_db()
    return g.PSQL
@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'PSQL'):
        g.PSQL.close()
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
    return "<h1 style='color:blue'>Hello There!</h1>"

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
    db = connect_db()
    userid = request.form['id']
    cur = db.cursor()
    cur.execute('select count(*) from users where userid = \'%s\';'%userid)
    numuser = cur.fetchall()[0][0]
    if numuser == 1:
        if request.method =='POST':
            rate = request.form['rates']
            userid = request.form['id']
            dic = eval(rate)
            calculate(dic)
            response = app.response_class(
            status=200,
            mimetype='application/json')
            return response
    else:
        response = app.response_class(
            status=404,
            mimetype='application/json')
        return response
@app.route('/getgames',methods = ['POST'])
def getgames():
    if request.method =='POST':
        db = connect_db()
        userid = request.form['id']
        cur = db.cursor()
        cur.execute('select count(*) from users where userid = \'%s\';'%userid)
        numuser = cur.fetchall()[0][0]
        if numuser == 1:
            cur.execute("select count(*) from games;")
            numgame = cur.fetchall()[0][0]
            ran = range(numgame)
            li = random.sample(ran, 10)
            sIdList = []
            idList = []
            for i in li:
                cur.execute('select id,steamid from games where id=\'%s\';'%i)
                ids = cur.fetchall()[0]
                id = ids[0]
                idList.append(id)
                gameid = ids[1]
                sIdList.append(gameid)
            dic = {'sid':sIdList,'id':idList}
            response = app.response_class(
            response = json.dumps(dic),
            status=200,
            mimetype='application/json')
            return response
        else:
            response = app.response_class(
            status=404,
            mimetype='application/json')
            return response
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))
