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
@game_blue_print.route('/calrate',methods = ['POST'])
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
            reLi = calculate(dic)
            dic = {'sid':reLi}
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
