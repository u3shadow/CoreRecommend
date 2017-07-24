import  os
import random
import numpy as n
import scipy.io as io

def loadMovieList():
    fid = open("game_id.txt")
    n1 = 100
    movieList = [[] for i in range(n1)]
    for i in range(0,n1):
        line = fid.readline()
        indx = line.index(" ")
        idx = line[0:indx]
        movieName = line[indx:]
        movieList[i].append(movieName.strip())
    fid.close()
    return movieList

movieList = loadMovieList()
my_ratings = n.zeros((100,1))
ran = range(100)
li = random.sample(ran,10)
for i in range(0,10):
    print "please input score for %s (1-5)"%movieList[li[i]]
    s = input()
    my_ratings[li[i]] = s
ratting = {'my_ratings':my_ratings}
io.savemat("my_ratting.mat",ratting)

os.system("octave --no-gui ex8_cofi.m")
print "learn finish"
