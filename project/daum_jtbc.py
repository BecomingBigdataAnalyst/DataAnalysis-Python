import requests
from bs4 import BeautifulSoup

#다음 JTBC 뉴스 스크래핑 예제
#media.daum.net/cp/310
#	?page=2&regDate=20170105&cateId=1002

press = [310]       #언론사
date = [20180205]   #년월일
page = [1, 2, 3]    #페이지

news_title = []      #뉴스 제목
news_desc = []       #뉴스 간략소개

URL = 'http://media.daum.net/cp/' + str(press[0]) + \
      '?page' + str(page[0]) + '&regDate=' + str(date[0])


#스크래핑 해서 소스를 source_code 에 저장
source_code = requests.get( URL )

#중간 결과 출력
#print(source_code.text)

#텍스트 추출을 위해 lxml로 태그 분석(메모리 적재)후
plain_text = source_code.text
soup = BeautifulSoup(plain_text , 'lxml')

#기사 제목 추출
cnt = 1
for title in soup.select("a['class=link_txt']") :
    if (cnt > 15) : break
    #print(title.text.strip())
    news_title.append(title.text.strip())
    cnt += 1

#기사 간단소개 추출
cnt = 1
for title in soup.select("span['class=link_txt']"):
   if (cnt > 15): break
   # print(title.text.strip())
   news_desc.append(title.text.strip())
   cnt += 1


for i in range(0, 15):
   print(news_title[i])
   print("%s\n" %(news_desc[i]))