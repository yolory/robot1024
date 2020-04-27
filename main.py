import os
import json
import time
from selenium import webdriver
from time import sleep
import random
import datetime

home_url = 'http://t66y.com/thread0806.php?fid=7'

dr = webdriver.Chrome()
dr.get(home_url)
print("请先手动登录")
os.system('pause')
print("开始自动回复")

def format_date():
	return time.strftime("%Y-%m-%d %H:%M:%S")

def randomReply():
	f = open('reply.json', 'r', encoding='utf-8')
	replies = json.loads(f.read())
	return replies[random.randint(0, len(replies) - 1)]

def reply():
	tr3s = dr.find_elements_by_css_selector(".tr3.t_one.tac")
	tr3 = tr3s[-1] # 最后一行
	tds = tr3.find_elements_by_xpath("./*")
	a = tds[1].find_element_by_tag_name("a")
	href = a.get_attribute("href") # 获取链接
	dr.get(href)
	textarea = dr.find_element_by_name("atc_content") # 输入框
	s = randomReply()
	textarea.send_keys(s)
	btn = dr.find_element_by_name("Submit")
	btn.click()
	print(format_date(), "回复", s, href)
	return s

start_hour = 9
today_count = 0

while True:
	now = datetime.datetime.now()
	dr.get(home_url)
	if now.hour < start_hour:
		today_count = 0
		print(format_date(), "未到时间")
	elif today_count < 10:
		s = reply()
		
		today_count = today_count + 1
	else:
		print(format_date(), "今天的回帖上限已到")
	sleep(30*60) # 半小时回复一次

# dr.close()
