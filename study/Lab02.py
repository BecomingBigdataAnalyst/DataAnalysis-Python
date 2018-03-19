# 18 연봉계산
salary=int(input('연봉을 입력하세요'))
ismarried=input('결혼했나요? (Y/N)')
tax=0

if ismarried.upper() == 'N':

    if salary < 3000:
        tax = salary * 0.1
    else:
        tax = salary * 0.25

else:
    if salary < 6000:
        tax = salary * 0.1
    else:
        tax = salary * 0.25

print(ismarried, salary, tax)


#19 윤년 계산
year= input('윤년여부를 알고 싶은 년도를 입력하세요')

if year / 4 == 0 and year / 100 != 0 or year / 400 == 0:
    print('%d는 윤년입니다' % year)
else:
    print('%d는 윤년아닙니다' % year)


#20 복권발행
#이걸 할때는 []은 문자열만 인식한다
#숫자로 하고 싶다면 나누기를 해서 나오는 나머지를 가지고 계산해야한다.
print('#20 복권 발행')
import random

lotto = str(random.randint(100, 999))
lucky = str(input('복권 숫자 3자리를 입력하세요\n'))
match = 0 #일치여부

if lotto[0] == lucky[0] or lotto[0] == lucky[1] or lotto[0] == lucky[2]:
    match += 1
if lotto[1] == lucky[0] or lotto[1] == lucky[1] or lotto[1] == lucky[2]:
    match += 1
if lotto[2] == lucky[0] or lotto[2] == lucky[1] or lotto[2] == lucky[2]:
    match += 1

print(lotto, lucky, match)

if match == 3:
    print ('상금 1백만 지금')
elif match == 2:
    print('상금 1만 지급!')
elif match == 1:
    print ('상금 1천 지급')
else:
    print("꽝꽝꽝꽝꽝")

#21번 구구단
#숫자만 입력받기
#문자 - ASCII 코드값 : ord()
#ASCII 코드값 - 문자 : chr()
# 0: ASCII- 48, 9 : ASCII-57
dan = int(input('출력할 단은?'))
if ord(dan[0]) >= ord('0') and ord(dan[0]) <= ord('9'):
    print('구구단 출력')
else :
    print('입력 오류 - 숫자만 입력하세요!')

#22번 소문자를 대문자로 변환
#숫자나 대문자 입력시 오류메시지 출력
lower = input('소문자를 입력하세요~')
if ord(lower[0]) >= ord('a') and \
        ord(lower[0]) <= ord('z'):
    print(lower.upper())
else:
    print('소문자만 입력가능!!')


#23 숫자 맞추기
#1~100 사이 난수 생성 후 맞추는 게임


key = random.randint(1, 100)

while True:
    lucky = int(input('숫자 하나 입력해'))

    if key == lucky:
        print('빙고!!!')
        break;
    elif key < lucky:
        print('추측한 숫자는 이것보다 커요')
    else:
        print('추측한 숫자는 이것보다 작어요')

print('프로그램 종료.')


