import json

from flask import Blueprint, request
from flaskr import get_db,app

user_blue_print = Blueprint('blue_print', __name__,
                            template_folder='templates')
@user_blue_print.route('/login', methods=['GET', 'POST'])
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
            code = 200
        dic = {'code':code,'userid':userid}
        response = app.response_class(
            response=json.dumps(dic),
            status=200,
            mimetype='application/json')
        response.headers["Content-Type"]='application/json;charset=utf-8'
        return response
    else:
        dic = {'code':231}
        response = app.response_class(
            response=json.dumps(dic),
            status=400,
            mimetype='application/json')
        return response
@user_blue_print.route('/signup', methods=['POST'])
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
