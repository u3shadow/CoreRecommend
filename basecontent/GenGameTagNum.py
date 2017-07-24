import numpy as n
import scipy.io as sci
ftagnum = open("game_tag_s.txt")
fgame = open("game_id.txt")
ftag = open("tags.txt")
numgame = len(fgame.readlines())
numtag = len(ftag.readlines())
fgame.close()
ftag.close()
fgame = open("game_id.txt")
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
sci.savemat('ex8_movies.mat',dic)
ftagnum.close()
fgame.close()
ftag.close()