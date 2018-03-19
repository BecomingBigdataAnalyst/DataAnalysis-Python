#Pandas
#효과적인 데이터 분석 기능을 제공하는 패키지
#R에서 자주 사용하는 DataFrame을 파이썬에서도 사용할 수 있게 함

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

df = pd.read_excel('c:/JAVA/sungjuk.xlsx')
print(df)
#xlrd 패키지 설치 필요! - 엑셀 파일을 읽어 dataframe 으로 생성

#총점, 평균 계산 후 df에 추가           총점평균 구하기 위해 모든 축들을 다 sum해준다는것임
subj=['국어','영어','수학','과학']
df['총점']=df[subj].sum(axis=1)       #여기서부터 합쳐진다
df['평균']=df['총점']/len(subj)
df.sort_values(['평균'], ascending=[False]) #평균으로 정렬


import matplotlib as mpl #그래프 그리기
#font_name=mpl.font_mangaer.FontProperties(fname='c:/windows/fonts/malgun.ttf').get_name()
#mpl.rc('font',family=font_name)  #그래프 한글 설정

mpl.rc('font',family='Malgun Gothic')  #그래프 한글 설정

sj=df.sort_values(['평균'], ascending=[False])    #x,y축 설정해주고
sj.index = sj['이름']
sj['평균'].plot(kind='bar', figsize=(8,4))  #8x4사이즈로 종류느 막대기 차트로!

#DataFrame 객체 생성 : { 'key':['val','val', ...] }
data={'이름':['수지','혜교','지현'],
      '국어':[99,98,99],
      '영어':[55,77,88],
      '수학':[44,77,99]}

sj=pd.DataFrame(data)

print(sj)
print(sj['이름'])    #특정 컬럼만 보기


#Series : 1차원 자료구조, df에서 특정 컬럼 추출시 Series 생성
data = [4,5,6,7,8,9,10]
print(data)              #그냥 1차원 배열
print(pd.Series(data))   #행번호가 있는 다차원 배열

#데이터 프레임에 새로운 컬럼 추가
name=['수지','혜교','지현']
kor=[99,98,99],
eng=[55,77,88],
mat=[44,77,99]

data={'이름':name, '국어':kor, '영어':eng, '수학':mat}
sj=pd.DataFrame(data,columns=['이름','국어','영어','수학'])
print(sj)

gender=pd.Series(['남','여','여'])
sj['성별'] = gender
print(sj)

#dataFrame 행/열 삭제
sj = sj.drop(0,axis=0)        #첫번째 행 삭제
print(sj)

sj=sj.drop('성별',axis=1)     #'성별' 열 삭제
print(sj)

#아나콘다는 내가 주로 쓰는 패키지들을 미리 설치해서 빨리빨리 실행할 수 있도록 하는 것이고
#주피터는 R은 원래 내부적으로만 공유가 되었던 것인데 인터넷에서 코드를 올려서
#많은 사람들과 공유할 수 있도록 하는 것임!