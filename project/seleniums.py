#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

#selenium 설치
#firefox용 webdriver 다운로드

movie_rank=[]       #순위
movie_title = []    #제목
movie_grade = []    #평점
movie_opdate =[]    #개봉일


URL = 'http://movie.daum.net/main/new#slide-1-0'

#firefox를 띄워 브라우져에 나타난 소스를 스크래핑함
driver = webdriver.Firefox(
    executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
#웹브라우져를 자동화작업 할 수 있도록 특수하게 컴파일된
#브라우져인 geckodriver.exe을 다운로드 후 지정한 위치에 저장
#github.com/mozilla/geckodriver
driver.get(URL)

#source_code = requests.get(URL)
source_code = driver.page_source    #firefox로 가져온 소스를
                                    #source_code 변수에 저장
print(source_code)
soup = BeautifulSoup(source_code,'lxml')

#순위 추출
for i in range(1,21):
    findkey = 'em["class=num_rank rank_'+str(i).zfill(2)+'"]'
    for title in soup.select(findkey) :
        print("".join(title.text.strip().split()))

    #제목 추출
    findkey ="a['class=link_txt #top #ranking #title @1']"
    for title in soup.select(findkey):
        #print(title.text.strip())
        print(title.text.strip())