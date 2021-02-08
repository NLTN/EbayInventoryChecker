#!/usr/bin/env python3

# Nguyen Nguyen
# Feb 05, 2021
# Ebay Inventory Checker

import time  # Thread: Sleep
import datetime
import schedule  # Scheduler
import os  # Operating System , File system
import urllib3
from bs4 import BeautifulSoup

def yellow(text):
	return '\033[0;33m' + text

def red(text):
	return '\033[0;31m' + text

def green(text):
	return '\033[0;32m' + text

def white(text):
	return '\033[0;37m' + text

def run():
	print(yellow('\n\n***** Ebay\Adorama ' + datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S') + ' *****'))
	check_item_instock('https://www.ebay.com/itm/MSI-GeForce-RTX-3060-Ti-Gaming-X-Trio-8GB-GDDR6-Graphics-Card-3x-DisplayPort-/373450606733')

def check_item_instock(url):
	http = urllib3.PoolManager()
	response = http.request('GET', url)
	soup = BeautifulSoup(response.data, 'html.parser')

	htmlEle_title = soup.find("meta", {"name": "twitter:title"})['content']
	htmlEle_price = soup.find("span", {"id": "prcIsum"}).contents[0]
	htmlEle_inventory_status = soup.find("span", {"id": "qtySubTxt"}).find('span').contents[0].strip()
	
	print(white(htmlEle_title))

	if (htmlEle_inventory_status != '0 available'):
		print(green('price: {}, quantity: {}'.format(htmlEle_price, htmlEle_inventory_status)))
		os.system('afplay alarm_music.mp3') #play sound
	else:
		print(red('price: {}, quantity: {}'.format(htmlEle_price, htmlEle_inventory_status)))


# Testing Area
#check_item_instock('https://www.ebay.com/itm/MSI-GeForce-RTX-3060-Ti-Gaming-X-Trio-8GB-GDDR6-Graphics-Card-3x-DisplayPort-/373450606733')

# Setup Schedule.
schedule.every().minute.at(":00").do(run)
schedule.every().minute.at(":15").do(run)
schedule.every().minute.at(":30").do(run)
schedule.every().minute.at(":45").do(run)

while True:
    schedule.run_pending()
    time.sleep(1)