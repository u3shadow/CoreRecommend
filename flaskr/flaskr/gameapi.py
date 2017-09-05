import json
import random
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
sys.path.append('/home/u3/app/CoreRecommend')
sys.path.append('/home/u3-linux/PycharmProjects/CoreRecommend')
from flask import Blueprint, request
from flaskr import get_db, app, connect_db
from basecontent.MainToFlask import calculate

game_blue_print = Blueprint('game_blue_print', __name__,
                        template_folder='templates')
@game_blue_print.route('/getgames',methods = ['POST'])
def getgames():
    if request.method =='POST':
        userid = request.form['id']
        numuser = exSQLFind('select count(*) from users where userid = \'%s\';'%userid)
        if numuser == 1:
            numgame = exSQLFind("select count(*) from games;")
            ran = range(numgame)
            li = random.sample(ran, 10)
            sIdList = []
            idList = []
            db = get_db()
            cursor = db.cursor()
            for i in li:
                cursor.execute('select id,steamid from games where id=\'%s\';'%i)
                ids = cursor.fetchall()[0]
                id = ids[0]
                idList.append(id)
                gameid = ids[1]
                sIdList.append(gameid)
            dic = {'sid':sIdList,'id':idList}
            response = getResponse(dic,200)
            return response
        else:
            response = getResponse('',404)
            return response
@game_blue_print.route('/calrate',methods = ['POST'])
def calrate():
    userid = request.form['id']
    numuser = exSQLFind('select count(*) from users where userid = \'%s\';'%userid)
    if numuser == 1:
        if request.method =='POST':
            rate = request.form['rates']
            dic = eval(rate)
            reLi = calculate(dic)
            dic = {'sid':reLi}
            response = getResponse(dic,200)
            return response
    else:
        response = getResponse("",404)
        return response

def exSQLFind(str):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(str)
    return cursor.fetchall()[0][0]

def getResponse(dic,status):
    if dic != '':
        response = app.response_class(
            response=json.dumps(dic),
            status=status,
            mimetype='application/json')
    else:
        response = app.response_class(
            status=status,
            mimetype='application/json')
    response.headers["Content-Type"]='application/json;charset=utf-8'
    return response
