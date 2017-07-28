# -*- coding=UTF-8 -*-
import json
import sys
from collections import OrderedDict
from GetScore import getScore

URL = 'http://steamspy.com/api.php?request=all'

def better_print(json_str):
	list =  json.loads(json_str,object_pairs_hook=OrderedDict)
	game_id = open("game_id.txt",'wb')
	game_tag_s= open("game_tag_s.txt",'wb')
	#print list[0]['tags'][0]
	i = 0
   	for (k) in list:
		i = i + 1
 		game_id.write("%d %s\n"%(i,list[k]['name']))
		score = getScore(list[k]['tags'],list[k]['owners'])
		game_tag_s.write("%s\n"%score)
	game_id.close()
	game_tag_s.close()

reload(sys)
sys.setdefaultencoding('utf-8')
jsons = open("gamejson.txt")
jsonstr = jsons.read()
better_print(jsonstr)
