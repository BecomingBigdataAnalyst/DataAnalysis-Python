#파이썬 자료구조
#리스트 : sequence 자료구조를 사용
#sequence : 순서가 있는 데이터 구조를 의미
#리스트, 튜플, 레인지, 문자열 등이 sequence 구조 사용
#리스트는 []을 이용해서 각 요소에 접근할 수 있다.
msg = 'Hello, World!!'

#파이썬에서는 자료구조를 의미하는 접미사를
#변수명에 사용하기도 한다
list1_list = []                  #빈리스트
list2_list= [1,2,3,4,5]         #숫자
list3_list = ['a','b','c']       #문자
list4_list = ['a','b', 'c',1,2,3,True] #혼합


print(list1_list)
print(list2_list)
print(list3_list)
print(list4_list)

#간단한 연산
#요소 존재 여부 파악: in/not in 연산자
print(1 in list1_list)
print('a' in list1_list)
print(3 in list2_list)

#길이 연산: len()
print(len( list1_list))
print(len( list2_list))

#연결 연산 : +
print( list2_list + list3_list)

#반복 연산 : *
print( list2_list * 2)

#요소의 특정값 참조: index 사용
print(msg[4], msg[9])
print(list2_list[2])
print(list3_list[2])
print(list4_list[5])

#요소값 변경 : index, = 사용
list2_list[2] = -3
print(list2_list)

#주민코드에서 성별 여부 판별
jumin=[1,2,3,4,5,6,1,2,3,4,5,6,7]
if jumin[6] == 1 :
    print('남자입니다')
else :
    print('여자입니다')


#주민코드에서 생년월일 추출
for i in range(0,6):
    print(jumin[i], end = ' ')
    #줄바꿈없이 출력시 종결문자를 지정

#특정범위내 요소들을 추출할때는 슬라이스를 사용 [i:j:step]
print(jumin[0:6])       #생년월일
print(jumin[:6])
print(jumin[6:])        #생년월일 제외 나머지부분
print(jumin[:])         #모두

print(jumin[0:6:2])       #홀수자리만 추출 1부터 6까지 2개씩 건너뛰어서 추출해준다.
print(jumin[::-1])          #역순 출력

#print(jumin[100])       #인덱스 초과 - 오류? 실행안됌
#print(jumin[0:100:2])   #인덱스 초과 - 오류? 실행안됌

#리스트관련 통계함수
print(sum(list2_list))
print(min(list2_list))
print(max(list2_list))

#리스트가 주어지면
#이것의 가운데에 있는 요소값을 출력
#[1,2,6,8,4] => 6
#[1,2,6,8,4,10] => 6,8

#list = [1,2,3,4,5]
list = [1,2,3,4,5,6]
size = len(list)
mid = int(size/2)
#print('가운데 값:', list[mid]) #요소 추가 홀수
#print('가운데 값: ', list[mid-1], list[mid])
print('가운데 값: ', list[mid-1 : mid+1]) #요소 추가 짝수

def listcenter(list):
    size = len(list)
    mid = int(size / 2)
    if size %2 == 0: #짝수인 경우
        print(list[mid-1:mid+1])
    else:
        print(list[mid])

listcenter([1,2,3])
listcenter([1,2,3,4])

#리스트 조작 함수
#요소 추가: append
list = [1,2,3,4,5]
list.append(9)
list.append(8)
print(list)

#요소 추가 insert(위치, 값)
list.insert(6, 7)
print(list)

#요소제거: remove(값), 왼쪽부터 제거
list.remove(9)
print(list)

#요소제거 : pop(), pop(위치)
list.pop(5)
print(list)

list.pop()  #마지막 요소 제거
print(list)

#모두 제거: clear()
list.clear()
print(list)

#### 튜플 tuple
#리스트 자료구조와 유사하지만
#한번 입력한 자료는 변경불가
#즉, 요소 추가는 가능/ 수정,삭제는 불가
#튜플은()을 이용해서
#튜플 생성시 단일 요소는 요소 뒤에 , 를 추가

t=[1,2,3]       #리스트
t=(1,2,3)
t=(1,'a',True)  
t=(1)           #숫자
t=(1,)          #단일요소로 구성된 튜플
print(t)
days = ('일','월','화', '수', '목', '금')
print(days)     #요일을 튜플로 정의하고 출력

print(days[3])      #'수'요일 출력
print(len(days))
print(days[3:])     #슬라이스

#days[3] = '水'      #튜플요소에 값 변경 - 불가!

#### 집합set
#저장된 데이터를 순서에 따라 관리 하지 않고
#중복을 허용하지 않는 자료구조
#집합은 {}을 이용 
#집합의 개념에 따라 합/교/차집합등의 연산 지원


t=[1,1,1,1]
print(t)

t=(1,1,1,1)
print(t)

t={1,1,1,1}
print(t)

t=[1,1,1,3,5,6,7,3,3,2,5,7,8,9,]
print(t)

t = set(t) #리스트를 집합으로 변환
print(t)    #집합은 중복된 자료들을 없애준다!!!! 그리고 데이터순서와도 상관없이 작은자료들부터 출력한다

#집합 정의
#1월 중 교육받은 날을 집합으로 정의
edu={1,2,3,4,5,8,9,10,11,12,15,16,17,18,19,22,23,24,25,26,29,30,31}
print(edu)
#집합의 기본적인 연산
동물={'사자', '늑대', '호랑이', '얼룩말'}
육상동물 = {'기린','여우','토끼'}
해상동물 = {'고래', '상어', '고등어','갈치'}
조류 = {'독수리','참새','부엉이'}

print(len(동물))     #길이
print('여우' in 육상동물)             #여우 검색 : in연산자
print('여우' in 조류)
#print(동물[2])             #인덱스 연산: 3번째 동물은?

print(육상동물.union(해상동물))         #합집합
print(육상동물 | 해상동물)              #합집합

새로운동물 = 육상동물 | 해상동물
print(새로운동물.intersection(육상동물)) #교집합
print(새로운동물.intersection(해상동물)) #교집합
print(새로운동물 & (해상동물))           #교집합

print(새로운동물.difference(육상동물))   #차집합
print(새로운동물.difference(해상동물))   #차집합
print(새로운동물-해상동물)               #차집합

print(새로운동물.symmetric_difference(육상동물))   #대칭차집합
print(새로운동물^육상동물)                         #대칭차집합


#집합에서 제공하는 메서드
동물.add('인간')        #데이터 추가
print(동물)


동물.discard('인간')    #데이터 제거
print(동물)


해상동물.remove('고등어') #데이터 제거
print(해상동물)


print(육상동물.pop())    #데이터 확인 후 제거
print(육상동물)


동물.clear()             #데이터 모두 제거
print(동물)

#패킹, 언패킹
#패킹packing: 여러 데이터를 변수 하나에 묶어 담기
#언패킹unpacking : 변수에 담긴 데이털르 여러 변수에 풀어 놓기

numbers = (1,2,3,4,5)   #튜플 생성 (packing)
a,b,c,d,e = numbers     #튜플에 저장된 데이터를 언패킹
print(c)

numbers = 1,2,3,4,5     #패킹시 () 생략 가능

#x,y,z = numbers         #언패킹시 데이터수와 변수갯수 일치

x,y,*z = numbers         #언패킹시 불일치시 처리방법
print(z)

# n, k, e, m = input().split()

a, b, c = 1, 2, 3       #변수 초기화에 패킹, 언패킹 사용



#연습문제 풀이
x = [1,2,3,4,5,6,7,8,9]

print(x)
x.append(10)            #요소 하나를 리스트에 추가
print(x)

x.extend([11,12])       #하나 이상 요소를 리스트에 추가
print(x)

x.remove(11)            #값을 제거
x.remove(12)
print(x)

x.reverse()             #요소를 역순으로 배치
print(x)

print(x.pop())
print(x)

x=[10,5,4,1]            #정렬안된 리스트
print(x)

x.sort()                #리스트 정렬
print(x)

 # 1,4,5,10
x.insert(3,7)           #10앞에 7을 삽입
print(x)

print(x.count(4))       #지정한 요소 수
print(x.index(5))       #요소의 위치값 출력

z = {1,1,1,2,2,3,3,3}
print(z)                #요소는 모두 3개

z.add(1)                #의미 없는 코드
print(z)                #어쨌든 3개

