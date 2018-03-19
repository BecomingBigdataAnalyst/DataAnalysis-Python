#Matplotlib
#파이썬에서 데이터과학 관련 시각화 패키지

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#%matplotlib inline #주피터노트북에서 그래프 그릴때
#show() 호출없이도 #그래프를 그릴수 있게 해줌
data=np.arange(10)
plt.plot(data)
plt.show()

#산점도 - 100의 표준정규분포 난수 생성
list=[]
for i in range(100) :           #0~99
    x = np.random.normal(0,1)   #표준정규분포 난수
    y = x+0.1+0.2+ np.random.normal(0,1)
    list.append([x,y])


    x_data= [v[0] for v in list]  #v=[x,]
    y_data =[v[1] for v in list]  #v=[,y]

plt.plot(x_data,y_data,'ro')
plt.show()

df = pd.read_excel('c:/JAVA/sungjuk.xlsx')

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

# 성적 비교 - 어느 반이 잘했나?
ban1 = df[df['반']==1]
ban2 = df[df['반']==2]
ban1_mean = ban1['총점'].sum() / (6*4)
ban2_mean = ban2['총점'].sum() / (6*4)
print(ban1_mean, ban2_mean)  #79.042 vs 77.125

#두 집단 간의 평균은 유의미하게 차이 나는것인가? (t검증)
#p-value 값이 0.005 이하 일때 - 차이가 난다고 할 수 있음
import scipy.stats as stats
result=stats.ttest_ind(ban1['평균'],ban2['평균'])
print(result)    #pvalue=0.755583336185639 (귀무가설이 오류가 날 확률)

#과목별 평균은 차이가 나는가? (t검증)
for sub in subj:
    print(sub,stats.ttest_ind(ban1[sub],ban2[sub]))

#국어 pvalue=0.031982494983816424
#영어 pvalue=0.5518533781528807
#수학 pvalue=0.1654958420079056
#과학 pvalue=0.0014931977711732465

#전체 성적데이터에 대한 그래프 출력
#sj_gph=sj.plot(kind='bar',figsize=(10,6))
#plt.plot(sj, figsize=(10,6))
sj[subj].plot(kind='bar',figsize=(10,6))

#과목별 점수 분포 - 박스수염 그래프 작성
df[subj].boxplot(return_type='axes')

#1반, 2반 과목별 점수 분포
ban1[subj].boxplot(return_type='axes') #1반
ban2[subj].boxplot(return_type='axes') #2반

#과목별 상관관계 -'수학:과학' 와 '국어:영어'
df.plot(kind='scatter',x='수학',y='과학')
print(stats.pearsonr(df['수학'],df['과학']))  #피어슨 상관계수
#(0.5632890597067751 (상관계수) 0.05650580486155532(p검증값)

df.plot(kind='scatter',x='국어',y='영어')



