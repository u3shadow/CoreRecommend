# -*- coding=UTF-8 -*-
import json
import sys
from collections import OrderedDict
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from datainitscript.GetScore import getScore
from dbscript.DBmethods import connect_db

URL = 'http://steamspy.com/api.php?request=all'

def init_data(json_str):
    list =  json.loads(json_str,object_pairs_hook=OrderedDict)
    db = connect_db()
    cur = db.cursor()
    game_tag_s= open("game_tag_s.txt",'wb')
    for (k) in list:
        if list[k]['appid'] != 999999:
            id = int(list[k]['appid'])
            name = str(list[k]['name'])
            cur.execute('insert into games(name,steamid) values(%s,%s)',[name,id])
            score = getScore(list[k]['tags'],list[k]['owners'])
            game_tag_s.write("%s\n"%score)
    db.commit()
    game_tag_s.close()
    db.close()

reload(sys)
sys.setdefaultencoding('utf-8')
jsons = open("gamejson.txt")
jsonstr = jsons.read()
init_data(jsonstr)
print "init finish"
