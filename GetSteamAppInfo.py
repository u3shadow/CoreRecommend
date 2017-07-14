import json
import requests
from collections import OrderedDict

URL = 'http://steamspy.com/api.php?request=top100in2weeks'

def better_print(json_str):
	list =  json.loads(json_str,object_pairs_hook=OrderedDict)
	game_id = open("game_id.txt",'wb')
	i = 0
   	for (k) in list:
		i = i + 1
 		game_id.write("%d %s %s\n"%(i,list[k]['name'],list[k]['score_rank']))
		print list[k]['name']
	game_id.close()


def request_get_method():
	response = requests.get(URL)
	print better_print(response.text)

request_get_method()
print ''