#coding:utf-8
import requests
import json
import time
import random
import ConfigParser 


# room_id = '131254'
print '若直播地址为：https://www.zhibo8.cc/zhibo/nba/2019/0105131254.htm，131254 则为房间号'
print '输入房间号：'
room_id = raw_input()

config = ConfigParser.ConfigParser()
config.readfp(open('cfg.ini'))
max_id_url = config.get("zhibo8","max_id_url").replace('${room_id}',room_id)

txt_url = config.get("zhibo8","txt_url").replace('${room_id}',room_id)

headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

response  = requests.get(max_id_url,headers=headers)

max_id = response.text

# print max_id

for i in range(int(max_id),10000,2):

	id = 0
	if i%2==1:
		id = i-1
	else:
		id = i

	url = txt_url+str(id)+'.htm'

	while True:

		# print url
		response  = requests.get(url,headers=headers)

		# print response.status_code,type(response.status_code)
		if response.status_code == 200:
			break;
		time.sleep(random.uniform(1.1,2.1)) 
				


	text = json.loads(response.text)

	for v in text:
		print v.get('user_chn')+':'+ v.get('live_text')

	time.sleep(random.uniform(1.1,2.1)) 

