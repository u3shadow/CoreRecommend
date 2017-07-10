import  os
import numpy as n
import scipy.io as io

my_ratings = n.zeros((1682,1))
my_ratings[1] = 4
my_ratings[98] = 2
my_ratings[7] = 3
my_ratings[12]= 5
my_ratings[54] = 4
my_ratings[64]= 5
my_ratings[66]= 3
my_ratings[69] = 5
my_ratings[183] = 4
my_ratings[226] = 5
my_ratings[355]= 5
ratting = {'my_ratings':my_ratings}
io.savemat("my_ratting.mat",ratting)

os.system("octave --no-gui ex8_cofi.m")
print "learn finish"