from random import randint
import scipy.io as sci
import numpy as n



Y =  n.zeros((14329,10000))
def initScore(row,score):
    total = score / 20 * 10000
    left = total
    for i in range(0, 10000):
        score = randint(0, 5)
        if left > 0:
            Y[row][i] = score
            left = left - score
        else:
            break;
    while left >= 0:
        score = randint(0, 5)
        for j in range(0, 10000):
            if Y[row][j] + score <= 5:
                Y[row][j] = score + Y[row][j]
                left = left - score
                break;
    print left

game_sco = open("game_sco.txt")
score = game_sco.readline()
i = 0
while score != '':
    print i
    initScore(i,int(score))
    i = i + 1
    score = game_sco.readline()
dic = {"Y":Y}
sci.savemat("ex8_movies.mat",dic)




