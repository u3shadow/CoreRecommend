import  os
import sys


curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import numpy as n
import scipy.io as io
from LoadGameFile import loadGameList
from basecontent.dbscript.DBmethods import connect_db

def calculate(rate):

    path = os.path.split(os.path.realpath(__file__))[0]+"/"
    os.chdir(path)
    tup = loadGameList()
    numgame = tup[1]
    my_ratings = n.zeros((numgame,1))
    print numgame
    for (k,v) in rate.items():
        my_ratings[int(k)] = int(v)
    ratting = {'my_ratings':my_ratings}
    io.savemat("my_ratting.mat",ratting)
    os.system("octave --no-gui ex8_cofi.m")
    result = open("result.txt",'wb')
    reLi =[]
    db = connect_db()
    cur = db.cursor()
    for line in result.readlines():
        if line.startswith("#") == False and len(line.split()) >0:
            d = int(line)
            cur.execute('select steamid from games where id=\'%s\''%d)
            sid = (cur.fetchall())[0][0]
            reLi.append(sid)
    db.close()
    os.remove("result.txt")
    os.remove("my_ratting.mat")
    return reLi




