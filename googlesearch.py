from selenium import webdriver
from selenium.webdriver.common.keys import Keys #자동완성기능 import
import time

#import bs4
#soup = bs4.BeautifulSoup()

#from bs4 import BeatifulSoup
#soup = BeautifulSoup()
#bs4모듈 내에서 필요한 기능만 빼와서 쓰는 것, bs4내의 다른 기능은 못쓴다

path = './chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('https://www.google.com/')
time.sleep(3)   #구글 홈페이지가 뜨기를 기다림

search_input = driver.find_element_by_css_selector('#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')

search_input.send_keys('HelloWorld')
search_input.send_keys(Keys.RETURN) #위에 친 단어를 자동완성 시킨 뒤 RETURN이 엔터 역할로 찾아들어간다
search_input.get_attribute()
#tsf > div:nth-child(2) > div.A8SBwf.emcav > div.RNNXgb > div > div.a4bIc > input   //일반 크롬 서치 셀렉터
#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input //자동화로 켜진 크롬 서치 셀렉터