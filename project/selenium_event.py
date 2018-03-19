#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver


#탐색할 URL 정의
URL = 'https://kr.investing.com/currencies/'

#웹 브라우저 자동화를 위해 웹 드라이버 초기화
driver = webdriver.Firefox( executable_path=
        r'C:\Program Files\Mozilla Firefox\geckodriver.exe')

#브라우저를 지정한 URL로 이동시킴
driver.get(URL)

#웹 페이지 오른쪽 '암호화폐' 탭의 xpath정의
# //*[@id="QBS_7"]
# /html/body/div[5]/aside/div[2]/div[1]/ul/li[4]/a
alink = driver.find_element_by_xpath('//li[@id="QBS_7"]/a')

#마우스, 단축키 이벤트 처리를 위해 ActionChains 초기화
mouse = webdriver.ActionChains(driver)

#해당 링크를 마우스클릭으로 처리하기 위해 move_to_element 사용
#즉, 마우스를 링크로 이동한 다음 클릭
mouse.move_to_element(alink).click().perform()

#클릭후 보여지는 페이지 내용을 source_code에 저장
source_code = driver.page_source
#print(source_code)

#웹 페이지 내용을 parsing 하기 위해 bs4로 초기화
soup = BeautifulSoup(source_code,'html.parser')
btccode = ['-btc-usd','-btc-krw','-eth-usd']        #종목
btccurcode=['945629','940808','997650']    #환율코드

for i in range(0, len(btccode)):
        # 암호화페 종류 (data-gae="-btc-usd")
        findkey = 'a["data-gae='+ str(btccode[i])+'"]'
        for title in soup.select(findkey) :
                print((title.text).encode('utf-8'))

        #암호화페 환율 (id="sb_last_945629")
        findkey = 'td["id=sb_last_'+str(btccurcode[i])+'"]'
        for title in soup.select(findkey):
                print(title.text)

#종목추출

#테스트를 위해 띄운 브라우져 닫기
driver.close()