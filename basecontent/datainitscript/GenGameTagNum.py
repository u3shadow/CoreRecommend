import numpy as n
import scipy.io as sci
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from dbscript.DBmethods import connect_db
ftagnum = open("game_tag_s.txt")
ftag = open("tags.txt")
db = connect_db()
cur = db.cursor()
cur.execute('select count(*) from games')
numgame = cur.fetchall()[0][0]
print numgame
numtag = len(ftag.readlines())
ftag.close()
ftag = open("tags.txt")
Y = n.zeros((numgame,numtag))
for i in range(0,numgame):
    score = ftagnum.readline()
    if score != None and score != '':
        scores = score.split(":")
        for s in scores:
            if s != '':
                s = s.split(",")
                if len(s) == 2:
                    Y[i][int(s[0])] = int(s[1])
dic = {"Y":Y}
sci.savemat('../ex8_movies.mat',dic)
ftagnum.close()
ftag.close()
print "gen finish"