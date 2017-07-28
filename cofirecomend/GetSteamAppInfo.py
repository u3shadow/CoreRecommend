# -*- coding=UTF-8 -*-
import json
import sys
from collections import OrderedDict

URL = 'http://steamspy.com/api.php?request=all'

def better_print(json_str):
	list =  json.loads(json_str,object_pairs_hook=OrderedDict)
	game_id = open("game_id.txt",'wb')
	game_score = open("game_sco.txt",'wb')
	i = 0
   	for (k) in list:
		i = i + 1
 		game_id.write("%d %s\n"%(i,list[k]['name']))
		if list[k]['score_rank'] != "":
			game_score.write("%s\n"%list[k]['score_rank'])
		else:
			game_score.write("0\n")
	game_id.close()
	game_score.close()



reload(sys)
sys.setdefaultencoding('utf-8')
jsons = open("gamejson.txt")
jsonstr = jsons.read()
better_print(jsonstr)
print ''