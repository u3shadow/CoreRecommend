import json
import uuid

from flask import Blueprint, request
from flaskr import get_db,app

user_blue_print = Blueprint('blue_print', __name__,
                            template_folder='templates')
@user_blue_print.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        sum  = exSQLFind('select count(*) from users where name=\'%s\' and psw=\'%s\''%(request.form['name'],request.form['psw']))
        if sum == 0:
            code = 230
            userid = -1;
        else:
            userid =  exSQLFind('select userid from users where name=\'%s\' and psw=\'%s\''%(request.form['name'],request.form['psw']))
            code = 200
        dic = {'code':code,'userid':userid}
        response = getResponse(dic,200)
        return response
    else:
        dic = {'code':231}
        response = getResponse(dic,400)
        return response

@user_blue_print.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        name1 = request.form['name']
        psw = request.form['psw']
        email = request.form['email']

        sumname = exSQLFind('select COUNT(name) from users where name=\'%s\''%name1)
        sumemail = exSQLFind('select COUNT(email) from users where email=\'%s\''%email)
        code = 200
        if sumname > 0:
            code = 230
        if sumemail > 0:
            code = 231
        if code == 200:
            db = get_db()
            cursor = db.cursor()
            cursor.execute('insert into users (name,psw,email,userid) values (%s,%s,%s,%s)',
                 [name1,psw,email,str(uuid.uuid4())])
            db.commit()
        dic = {'code':code}
        response = getResponse(dic,200)
        return response

def exSQLFind(str):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(str)
    return cursor.fetchall()[0][0]

def getResponse(dic,status):
    response = app.response_class(
            response=json.dumps(dic),
            status=status,
            mimetype='application/json')
    response.headers["Content-Type"]='application/json;charset=utf-8'
    return response
