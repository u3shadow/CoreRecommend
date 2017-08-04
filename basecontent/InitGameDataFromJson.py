# -*- coding=UTF-8 -*-
import json
import sys
from dbscript.DBmethods import connect_db
from collections import OrderedDict
from GetScore import getScore

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
