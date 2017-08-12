import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from dbscript.DBmethods import connect_db

def loadGameList():

    db = connect_db()
    cur = db.cursor()
    cur.execute('select count(*) from games')
    numgame = (cur.fetchall())[0][0]
    print numgame
    gameList = [[] for i in range(numgame+1)]
    for i in range(1,numgame+1):
        cur.execute('select name from games where id = \'%s\''%i)
        gameName = cur.fetchall()[0][0]
        gameList[i].append(gameName.strip())
    return (gameList,numgame)
