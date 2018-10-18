import requests
from bs4 import BeautifulSoup as bs
import logging
import http.client
import time
from random import randint
import json
from proxymanager import ProxyManager
from fake_useragent import UserAgent

ua = UserAgent()
proxy_manager = ProxyManager('proxies.txt')



def getCurrentTime():
    return time.strftime("[%H:%M:%S]--------")

gmail      = "@gmail.com"#dont change

with open('config.json') as json_data_file:
	config = json.load(json_data_file)

CONFIG     = config["CONFIG"] 
beggmail   = CONFIG["beggmail"]
first_name =  CONFIG["first_name"]
last_name  = CONFIG["last_name"]
password   = CONFIG["password"]

print("{}Config Loaded".format(getCurrentTime()))



account_creation_link = 'https://undefeated.com/account/'

# Debug logging
#http.client.HTTPConnection.debuglevel = 1
#logging.basicConfig()
#logging.getLogger().setLevel(logging.DEBUG)
#req_log = logging.getLogger('requests.packages.urllib3')
#req_log.setLevel(logging.DEBUG)
#req_log.propagate = True

for x in range(10):
	RGmail = "{}+{}_{}{}".format(beggmail,(randint(0,99)),(randint(0,99)),gmail)
	random_proxy = proxy_manager.random_proxy()
	proxies = random_proxy.get_dict()
	print(proxies)
	session = requests.Session()
#	session.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}
	session.headers = {'User-Agent': ua.random}
	print(ua.random)
	#session.config['keep_alive'] = False
	
	
	payload1 = {
		"form_type":"create_customer",
		"utf8":"&#10004",
		"customer[first_name]":first_name,
		"customer[last_name]":last_name,
		"customer[email]":RGmail,
		"customer[password]":password
	}
#	print(payload1)
	account_post_response = session.post(account_creation_link, data=payload1, proxies=proxies)
#	print(account_post_response.text)
	#with open('account_post_response_{}.html'.format(x), 'w') as f:
	#	f.write(account_post_response.text)
	print(account_post_response.status_code)
	if "g-recaptcha" not in account_post_response.text:
		print(RGmail)
		with open('generated_accounts.txt', 'a') as fc:
			fc.write(RGmail + "\n")
	time.sleep(randint(5,10))
