#1  print()를 이용 다음 내용이 출력
print(  )
print('*   *')
print('*   *')
print('*****')
print('*   *')
print('*   *')


print('  **')
print(' *  *')
print('*    *')
print('******')
print('*    *')

print('****')
print('*   *')
print('****')
print('*   *')
print('*    *')

print('****')
print('*   *')
print('****')
print('*   *')
print('*    *')


print('*    *')
print('*    *')
print('  * * ')
print('   *  ')
print('   *  ')

print('   /////  ')
print(' |  o o  | ')
print('(|   ^   |)')
print(' |  [_]  |')
print('  _______')

print("            +---+");
print("            │   │");
print("        +---+---+");
print("        │   │   │");
print("    +---+---+---+     /\\_/\\      -----");
print("    │   │   │   │    ( ' ' )   / Hello \\");
print("+---+---+---+---+    (  -  )  <  Junior │");
print("+   │   │   │   │    │  │  │   \\ Coder!/");
print("+---+---+---+---+    (__│__)     -----");

# 2 이름, 나이, 몸무게
name = '혜교'
print(name)
weight = 55
print(weight)
age = 35
print('{},{},{}'.format(name,weight,age))


# 3 수학식을 파이썬 표현식으로 작성
x=2
y=3
z=4
print('3x=', 3*x)
print('3x+y=',3*x+y)
print('(x+y)/7=',(x+y)/7)
print('(3x+y)/(z+2)',(3*x+y)/(z+2))

# 4 다음 표현식을 완성
x,y=4,8
x *= y      # x = x*y
print('x *= y :',x )
x -= y
print('x -= y :',x)

# 5 다음 수식을 파이썬으로 작성
x = 3       # x =??
print(x+7 == 10)

# 6 다음 표현식의 결과는?
print((-32+95)*12/3)
print((3*4-((-27+67)/4))**8)
print((512+1968-432)/(2**4)+128)
print(256 == 2**8)
print(50+50 <= 10*10)
print(99 != 10**2-1)


# 7 다음 식의 실행결과는?
x = 2.5
y = -1.5
m = 18
n = 4
print(x+n*y-(x+n)*y)
print(m/n + m%n)
print(5*x-n/5)
print(1-(1-(1-(1-(1-n)))))

# 8 어느 방이 더 가격대비 더 넓은지 알아봐
a = (2.5 * 3) / 27
b = (4 * 2) / 30
print(a)
print(b)
# 한평당 A방이 더 싼편이며 B방이 500원정도 더 비싸다 즉 A방이 더 넓다

# 9
print( 3 + 4.5 * 2 + 27 / 8)
print( True or False and 3 < 4 or not (5 == 7))
print( True or (3 < 5 and 6 >= 2))
# print( not True > 'A') 문자에 비교 연산자
# print( 7 % 4 + 3 - 2 / 6 * 'Z') #문자에 산술연산자
# print('D' + 1 + 'M' % 2/3) #문자에 산술연산자
print( 5.0 / 3 + 3 / 3)
print( 53 % 21 < 45 / 18)
print((4 < 6) or True and False or False and (2 > 3))
print( 7 - ( 3 + 8 * 6 + 3) - (2 + 5 * 2))

# 10 이윤율 계산 - 도메인 문제
# 지문만으로는 문제를 해결할 수 없음
# 문제에 대한 배경지식이 필요 - 이윤율 공식
가변자본 =15
불변자본 =30
잉여가치 =45
이윤율 = 잉여가치 / (불변자본 /+ 가변자본)
print('이윤율 :', 이윤율)

x=(45/(15+45))
print(x) #0.75가 나온다


# 11 1달러 1071원 1유로 1309원
달러노트북 = 780 * 1070
유로노트북 = 650 * 1309
print( '달러노트북 %d, 유로 노트북 %d' \
       %(달러노트북, 유로노트북))
# 계산이 실행 안되므로 내가 구한다
# 650유로는 84만9998원이고
# 780달러는 83만4444원이다
# 그러므로 달러로 구매하는 개이득

# 12
#원의 둘레계산식:pi*지름
pi = 3.14
a = 50 * 2
b = 45 * 2
distance=바깥학생거리- 안쪽학생거리
print("바깥학생이 %d 미터 더 달렸음" % distance)

# 13 표현식 확인하기
print('Check out this line ')
# print('//hello there' + '9' + 7) #문자와 숫자간 산술연산
#print('H' + 'I' + "is" + 1 + "more example")
#print('H' + 6.5 + 'I' + "is" + 1 + "more example")
print("Print both of us", "Me too")
print("Reverse " + 'I' + 'T')
#print("Nonot Here is" + 1 + "more example")
#print("Here is " + 10*10)
#print("Not x is" + True) 문자와 블리언
print()
print   #함수의 유형 출력
#print("How about this one" ++ '?' + 'Huh?' ) # 증가연산자

# 14
print(True and False and True or True)
print(True or True and True and False)
print((True and False) or (True and not False) or (False and not False))
print((2<3) or (5>2) and not (4 == 4) or 9 != 4)
print(6 == 9 or 5 <6 and 8 < 4 or 4 > 3)

# 15
a= 27/13+4
print (a)
type(a)
b= 27/13+4.0
print(b)
type(b)
c= 42.7 % 3 +18
print(c)
type(c)
# d= (3<4) and 5/8
#print(d)
# type(d)
e= 23/5 + 23/5.0
print(e)
type(e)
#f= 2.0+'a'
#print(f)
#type(f)
#g= 2+'a'
#print(g)
#type(g)
#h= 'a'+'b'
#print(h)
#type(h)
#i= 'a' / 'b'
#print(i)
#type(i)
#j= 'a' and not 'b'
#print(j)
#type(j)
# k=(double)'a'/ 'b' 실수형으로 바꾸고 싶다면 float()실수변환 함수!
# type(k)

# 16
# 파이썬에서는 기본적으로 ++, --는 지우넝하지 않는다.
n=3
print(++n)  #+(+n), ++n, n-- 이런건 지원안한당!
print(--n)  #-(-n)
n+=1
print(n)
n=3
n-=1
print(n)

# 17 사칙연산 프로그램 - input 함수 이용
print('***사칙연산 프로그램 ***')
a=input('첫번째 정수를 입력하세요/n')
b=input('두번째 정수를 입력하세요/n')
print(int(a)+int(b))
print(int(a)-int(b))
print(int(a)*int(b))
print(int(a)/int(b))

num1 = int(input('첫번째 정수를 입력하세요'))
num2 = int(input('두번째 정수를 입력하세요'))
print('%d + %d = %d' % (num1, num2, num1 + num2))
print('%d + %d = %d' % (num1, num2, num1 - num2))
print('%d + %d = %d' % (num1, num2, num1 * num2))
print('%d + %d = %d' % (num1, num2, num1 / num2))













