import os


def loadGameList():

    path = os.path.split(os.path.realpath(__file__))[0]+"/"
    fid = open(path+"game_id.txt")
    numgame = len(fid.readlines())
    fid.close()
    fid = open(path+"game_id.txt")
    movieList = [[] for i in range(numgame)]
    for i in range(0,numgame):
        line = fid.readline()
        indx = line.index(" ")
        movieName = line[indx:]
        movieList[i].append(movieName.strip())
    fid.close()
    return (movieList,numgame)