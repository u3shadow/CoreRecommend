import  os
import random
import numpy as n
import scipy.io as io
import MySQLdb as mysql
from LoadGameFile import loadGameList
def connect_db():
    """Connects to the specific database."""
    rv = mysql.connect(host='localhost',user='root',passwd='u3shadow',db='test')
    return rv

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