# coding=UTF-8
import requests
import cookielib
import random
import urllib2
import uuid
import time
import os
from bs4 import BeautifulSoup
from bs4.builder._lxml import LXML
from selenium import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from __builtin__ import str

typeval =33
count = 0
i = 1
comickind = range(1,26)
for t in xrange(16,19):
	comickind.remove(t)
# print comickind

titlename = []
rest = requests.get("http://www.cococomic.com/")
intact_pag = rest.text.encode('iso-8859-1')
soupx = BeautifulSoup(intact_pag)
for t in xrange(4,26):
	titlename.append(soupx.select(u'.cHNav > div > a')[t].text)
# print titlename[15]

	
for x in comickind:
	for i in range(1,5): 
		
		from __builtin__ import str
		res = requests.get("http://www.cococomic.com/comiclist/"+str(x)+"/"+str(i))
		intact_page = res.text.encode('iso-8859-1')
		soup = BeautifulSoup(intact_page)
		for name in soup.select("div li a"):
			word = name.get("title")
			href = name.get("href")
			# print href
			resx = requests.get(href)
			intact_pagex = resx.text.encode('iso-8859-1')
			# resx.encoding = resx.apparent_encoding
			soupx = BeautifulSoup(intact_pagex, 'lxml')
			urltree = soupx.select(u'.cVolList > div > a')
			# imgneme = name.get("target")
			count = 1
			episode = []
			for z in xrange(len(urltree)):
			
				if (count == 1):
					comicurl = urltree[z]['href']
					episode = z
					count = 0
				count += 1
				# print urltree
				
				print(comicurl)
				# time.sleep(random.randint(4,8))
			# comires = requests.get(comicurl)
	# 		# print (comires)
			# comires.encoding = comires.apparent_encoding
			# soupex = BeautifulSoup(comires.text, 'lxml')
			# urlfour = soupex.select(u'.e > img ')
			# print (urlfour)
			# print(urlfour[0]['src'])
			# line = 1
			# for i in xrange(len(urlfour)):	
			# 	comicjpg = urlfour[i]['src']
			# 	# comicjpg = re.search(r'<img src="(.*?)".*?',re.S)
			# 	# imglink = jokes.get('src')
			# 	print(urlfour)
			# 	# print(comicjpg)
			# 	# print(imglink)
				browser = webdriver.Chrome()
				browser.get(comicurl)
				soup = BeautifulSoup(browser.page_source)
				pagenum = len(soup.select('.c select option'))
				print pagenum
				for i in xrange(1,pagenum+1):
					soup = BeautifulSoup(browser.page_source)
					for ele in soup.select('.e img'):
						eleurl=ele['src']
						print ele['src']
					
					temppath = titlename[x] + '/' + word +'/' + str(episode)

					if not(os.path.exists(temppath)):
						os.makedirs(temppath)
					
					f = open(temppath + '/' + str(i) + ".jpg" ,'wb')
					f.write(requests.get(eleurl).content)
					time.sleep(random.randint(1,2))
					if i!=pagenum:
						browser.find_element_by_css_selector("div.g > a.n").click()	
									
					f.close()
				
				browser.close()
				