def readTag():
    tags = open('tags.txt')
    tagArray = tags.read().split('\n')
    tags.close()
    return tagArray
def getTagId(tag,tagArray):
    return tagArray.index(tag)
def getTagScore(num,owner):
    score = num
    return score
def getScore(tagList,owner):
    str = ''
    tagArray = readTag()
    for (k) in tagList:
        id = getTagId(k,tagArray)
        score = getTagScore(tagList[k],owner)
        str += ":%d,%d:"%(id,score)
    return str
