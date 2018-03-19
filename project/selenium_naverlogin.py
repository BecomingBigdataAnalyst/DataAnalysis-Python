#-*- coding: utf-8 -*-
import time
from bs4 import BeautifulSoup
from selenium import webdriver

#포탈사이트에 로그인한 후 자신이 받은 메일 수 확인
URL = 'http://www.naver.com'

#웹 브라우저 자동화를 위해 웹 드라이버 초기화
driver = webdriver.Firefox( executable_path=
        'C:\Program Files\Mozilla Firefox\geckodriver.exe')

#브라우저를 지정한 URL로 이동시킴
driver.get(URL)


#로그인창에 아이디/비번 입력 후 로그인 버튼 클릭
#html요소 중 id가 id인 요소를 찾음
userid = driver.find_element_by_id('id')
# @id=id 인 요소에 아이디를 입력
userid.send_keys('jjh9523')

#html요소 중 id가 pw인 요소를 찾음
passwd = driver.find_element_by_id('pw')
#@id=pw 인 요소에 비밀번호를 입력
passwd.send_keys('cheerupjjh93@')

#로그인 버튼을 찾아 클릭
loginbtn = driver.find_element_by_xpath('//input[@title="로그인"]')
loginbtn.submit()

#처리속도가 빨라서 로그인완료 페이지가 뜨기전에
#메일 확인 페이지로 이동하려고 함 - 메일페이지가 제대로 안뜸

#따라서 로그인 완료 페이지가 뜨는걸 확인하기 위해
#(서버로부터 넘어오는 응답데이터를 다 받을때까지)
#일정시간 동안 브라우져를 잠시 대기시킴
#driver.implicitly_wait(3)
time.sleep(3)       #파이썬 처리를 지연

#메일 페이지로 이동
MailURL='https://mail.naver.com/?n=1518057925676&v=f'
driver.get(MailURL)

source_code = driver.page_source
soup = BeautifulSoup(source_code, 'html.parser')

#안 읽은 메일(span[class=cnt])
findkey = 'span["class=cnt"]'
for title in soup.select(findkey) :
    print(title.text)


#로그아웃버튼 클릭 - 로그아웃 처리
# time.sleep(3)
# mouse = webdriver.ActionChains(driver)
# logoutbtn = \
#     driver.find_element_by_xpath("//span[@id='gnb_name1']")
# mouse.move_to_element(logoutbtn).click().perform()
#
# time.sleep(3)
# logoutbtn = driver.find_element_by_id("gnb_logout_button")
# mouse.move_to_element(logoutbtn).click().perform()


time.sleep(3)
driver.get('https://nid.naver.com/nidlogin.logout?returl=http://mail.naver.com/login')
