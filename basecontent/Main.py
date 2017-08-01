import  os
import random
import numpy as n
import scipy.io as io
from LoadGameFile import loadGameList

numgame = 0
tup = loadGameList()
movieList = tup[0]
numgame = tup[1]
my_ratings = n.zeros((numgame,1))
ran = range(numgame)
li = random.sample(ran,10)
for i in range(0,10):
    print "please input score for %s (1-5)"%movieList[li[i]]
    s = input()
    my_ratings[li[i]] = s
ratting = {'my_ratings':my_ratings}
io.savemat("my_ratting.mat",ratting)

os.system("octave --no-gui ex8_cofi.m")
print "learn finish"
def calculate(rate):
    tup = loadGameList()
    numgame = tup[1]
    my_ratings = n.zeros((numgame,1))
    for (k,v) in rate.items:
        my_ratings[int(k)] = int(v)
    ratting = {'my_ratings':my_ratings}
    io.savemat("my_ratting.mat",ratting)
    os.system("octave --no-gui ex8_cofi.m")
