#numpy
#선형대수(배열,행렬) 연산에 효과적인 함수 제공
#리스트 자료구조와 유사 - 파이썬 리스트보다 속도가 빠름
#randn(행,열) : 다차원배열, 정규분포를 따르는 난수 생성
#array(리스트):다차원배열 생성
#arrange : 0~(n-1) 정수 생성

import Numpy as np
from Numpy import genfromtxt  #텍스트 파일을 배열로 생성


data = np.random.rand(3,4)   #3*4행렬에 난수 생성
print(data)

lotto=np.random.randint(46,size=(3,6))  #3*6행렬에 난수 생성
print(lotto)

list=[3,4.1,5,6.3,7,8.6]      #단일 리스트
arr=np.array(list)


print('평균',arr.mean())      #기술통계
print('합계',arr.sum())
print('합계',np.count_nonzero(arr))
print('최대값',arr.max())
print('최소값',arr.min())
print('분산',arr.var())
print('표준편차',arr.std())

list = [[9,8,7,6,5],[1,2,3,4,5] ]  #중첩리스트
arr = np.array(list)
print(arr)
print(arr[0,2])     #7
print(arr[1,3])     #4
print(arr[0,:])     #9 8 7 6 5 행 전체 출력
print(arr[:,1])     #8 2       열 전체 출력

#자동으로 채워지는 행렬 생성
zarr = np.zeros((3,5))   # 0으로 채워지는 3x5 행렬 생성

print(zarr)
#정수 생성
cnt = 0
for i in np.arange(3):
    for j in np.arange(5):
        cnt += 1
        zarr[i,j] = cnt

print(zarr)

#외부 csv 파일 읽어서 배열 생성
phone=genfromtxt('c:/JAVA/phone-01.csv', delimiter=',')
print(phone)
print(np.mean(phone[:,2])) #화면크기 항목에 대한 평균 출력
print(np.mean(phone[:,2])) #중앙값

print('총 갯수:', len(phone))

p_col3=phone[:,2]
np.percentile(p_col3,0)     #사분위값 : 최소값
np.percentile(p_col3,25)    #1사분위값 : 최소값
np.percentile(p_col3,50)    #2사분위값 : 최소값
np.percentile(p_col3,75)    #3사분위값 : 최소값
np.percentile(p_col3,100)   #사분위값 : 최대값

#scipy에는 여러가지 기술통계를 한번에 계산해주는
#describe 함수가 있음
from scipy.stats import describe
print(describe(p_col3))

