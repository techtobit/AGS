from selenium import webdriver
from helium import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
import time
import re



class Search:
	def __init__(self):

		# Use Helium 
		self.browser =  start_chrome(headless=True)

	def gSarch(self,keyword):
		go_to("https://www.google.com")
		search_box = find_all(S("textarea[name='q']"))[0]
		write('python', into=search_box)
		press(ENTER)
		time.sleep(3)

	def getResult(self):
		wait_until(lambda: len(find_all(S("cite"))) > 0, timeout_secs=10)
		elements = find_all(S("cite"))
		urls = []

		for element in elements:
			text=element.web_element.text.strip()
			match = re.match(r'https?://\S+', text)
			if match:
					urls.append(match.group(0)) 
		print(urls)

	def closeBrowser(self):
		kill_browser()



