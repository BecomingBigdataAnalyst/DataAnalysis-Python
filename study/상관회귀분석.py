#파일명 : 상관회귀분석.py
#파이썬으로 상관분석, 회귀분석 테스트
import numpy as np
import pandas as pd

#csv 파일 읽어오기
hdr=['V1','V2','V3','V4','V5','V6','V7','V8','V9']
df=pd.read_csv('c:/JAVA/phone-02.csv', header=None, names=hdr)
print(df)

#상관분석 실시
dfc=df.corr()
print(dfc)

#df97=df['V9'].corr(df['V7'])
df97=df.V9.corr(df['V7'])
print('핸드폰 사용량-데이터 소모량 관계 :',df97)

#회귀분석 실시
from scipy import stats
lm=stats.linregress(df.V7,df.V9)
#기울기, 절편,상관도,오류지수 p, 표준오차
print(lm)

#회귀식: y=절편+기울기x
#어떤 공장의 월별생산량과 전기사용량을 이용해서 회귀분석
#x:독립변수, y:종속변수
from scipy import polyval
make=[3.52,2.58,3.31,4.07,4.62,3.98,4.29,4.83,3.71,4.61,3.90,3.20]
            #단위:억
power=[2.48,2.27,2.47,2.77,2.98,3.05,3.18,3.46,3.03,3.25,2.67,2.53]

mp=pd.DataFrame()

기울기,절편,상관계수,p값,표준오차 \
=stats.linregress(make,power)
#회귀식 : y=절편+기울기x
#매출이 4억이면 전기사용량은 아마도??
예측전기사용량 = (절편+기울기*4)


#4.07:2.77,3.98 : 3.05
print(예측전기사용량)   #2.902

import matplotlib.pyplot as plt
import matplotlib

krfont={'family':'Malgun Gothic',
        'weight':'bold',
        'size':10}

matplotlib.rc('font',**krfont)


ry=polyval([기울기,절편],make)
plt.plot(make,power,'b.')  #파랑색 점 bo,b.,b^,b>,b1,bp,b*,bh,bD
plt.plot(make,ry,'r.-')    #빨간색 점, 실선 r. / r.-. / r-- / r.-/
plt.title('회귀분석 결과')
plt.legend(['실제 데이터','회귀분석을 따르는 모델'])
plt.show()