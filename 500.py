 #-*- coding: utf-8 -*-
#modules to import
import csv
import codecs
import urllib2
from bs4 import BeautifulSoup

with open('500.csv', 'w') as f:
	csvwriter = csv.writer(f)
	soup = BeautifulSoup(urllib2.urlopen('http://money.cnn.com/magazines/fortune/fortune500/2013/full_list/index.html?iid=F500_sp_full').read())
	header = soup.find(id='f500-list')
	body = soup.find(id="content-placeholder")

	for row in header.findAll('ul'):
		heads = [h.text for h in row.findAll('li')]
		csvwriter.writerow(heads)


	for row in body.findAll('li'):
		cells = [c.text.encode('utf-8') for c in row.findAll('span')]
		csvwriter.writerow(cells)

