#-*- coding: utf-8 -*-
#2.7버전에서만 위에 있는 글을 써줘야한다!
import requests
from bs4 import BeautifulSoup
import codecs
# 다음 영화 순위 스크래핑 예제
# movie.daum.net/main/new#slide-1-0
# http://ticket2.movie.daum.net/Movie/MovieRankList.aspx

# page = [0, 1, 2, 3, 4] # 페이지

movie_rank=[]       #순위
movie_title = []    #제목
movie_grade = []    #평점
movie_opdate =[]    #개봉일


URL = 'http://ticket2.movie.daum.net/Movie/MovieRankList.aspx'

# 스크래핑해서 소스를 에 저장
source_code = requests.get(URL)
# 중간 결과 출력
# print(source_code.text)
plain_text = source_code.text

soup = BeautifulSoup(plain_text,'html.parser')  #html 파서 (문법을 덜 따진다, 속도가 더 빠르다, 오류를 잡아주는건 힘듬)
#soup = BeautifulSoup(plain_text,'lxml')         #xml 파서 (문법까지 다 따져줘야한다, 오류를 잘 잡아줌, 성능은 좋음)
#print(soup)

#순위 추출
for i in range(1,21):
    findkey = 'span["class=ico_ranking ico_top'+str(i)+'"]'
    for title in soup.select(findkey) :
        #print(" ".join(title.text.strip().split()))
        movie_rank.append("".join(title.text.strip().split()))

#제목 추출
findkey ="a['class = link_g']"
for title in soup.select(findkey):
    #print(title.text.strip())
    movie_title.append(title.text.strip())

#평점 추출
findkey = "em['class = emph_grade']"
for title in soup.select(findkey):
    #print(title.text.strip()+"/10")
    movie_grade.append(title.text.strip())


#개봉일 추출
findkey = "dl['class=list_state']"
for title in soup.select(findkey):
    print(title.select('dd')[0].text)
    movie_opdate.append(title.text.strip())
#개봉날짜(dl)에서 첫번째에 나오는 dd를 갖고오기 위해서 인덱스에는 0을 넣어준 것임!!

#모든 내용 출력
for i in range(0,20) :
    print(movie_rank[i])
    print(movie_title[i])
    print(movie_grade[i])
    print( "%s\n" % (movie_opdate[i]))

#------파일 저장하기 -- 2.7버전으로 해야 한글이 안깨진다!
fmt = '%s,%s,%s,%s\n'   #출력형식 정의
f = open('movie_rank2.txt', 'w')        #파일을 쓰기모드로 open
for i in range(0,20):
    rank = fmt % (movie_rank[i], movie_title[i],\
            movie_grade[i], movie_opdate[i])
    #f.write(rank)  
    # #유니코드 문자 저장시 오류발생!! - codecs 추천!
    # 파이썬2는 기본적으로 모든 문자를 ascii(아스키)로 처리
    # 파일에 기록시 먼저 ascii로 디코딩 하기 때문에 오류발생!

#f.write('hello, python!! \n')           #파일에 내용쓰기
#f.write('안녕하세요, 파이썬!! \n')
f.close()                               #파일 작업종료 (필수!)

f = codecs.open('movie_rank2a.txt','w','utf-8') #오류발생없애기 위해 codecs 사용 (제목, 읽기모드, 유니코드)로 지정
for i in range(0,20):
    rank = fmt % (movie_rank[i], movie_title[i],\
            movie_grade[i], movie_opdate[i])
    f.write(rank)
f.close()


#------파일 저장하기 --(파이썬3)
#예외처리는 try ex를 사용한다!
try:
    f = open('movie_rank3.txt','w',encoding='utf-8')
    for i in range(0,20):
        rank = fmt % (movie_rank[i], movie_title[i],\
                movie_grade[i], movie_opdate[i])
        f.write(rank)
    f.close()
except Exception as ex:
    print(ex)

#---파일 읽어 출력하기 (파이썬2)
#readline   : 한줄씩 읽어옴(추가적으로 while 필요) (라인 하나)
#readlines  : 모든 줄을 리스트로 읽어옴(추가적으로 for 필요) (라인 전부 다 붙여서)
#read       : 파일 내용 전체 읽어옴 - 바이너리 파일 처리시 사용 (원본 그대로)

f = codecs.open('movie_rank2a.txt','r','utf-8')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()


f = codecs.open('movie_rank2a.txt','r','utf-8')
lines = f.readlines()
#print(lines)
#하나씩 출력하기
for line in lines:
    print(line)
f.close()

#원본그대로
f = codecs.open('movie_rank2a.txt','r','utf-8')
data = f.read()
print(data)
f.close()



#---파일 읽어 출력하기 (파이썬3)

f = open('movie_rank3.txt','r',encoding='utf-8')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

f = open('movie_rank3.txt','r',encoding='utf-8')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

f = open('movie_rank3.txt','r',encoding='utf-8')
data = f.read()
print(data)
f.close()

#with ~ as 구문으로 파일 다루기 (파이썬이 close를 자동으로 써주는 장점이 있음)
#파일 작업시 파일을 열고 닫는 것은 번거로운 일이므로
#파이썬이 알아서 닫아줘서 편리한 코드임
with codecs.open('movie_rank2a.txt','r','utf-8') as f :
    data = f.read()
    print(data)


#파일 읽기/쓰기 모드 
# r: read (읽기), w:write (쓰기)
# t: text (텍스트파일), b:binary ( 바이너리파일 : 이미지나 압축파일)
# a: append(추가),  + : update (수정)
# 파일모드의 기본값은 : rt
#