import random

#17 계산기 (제곱연산 추가)
def intCalu():
    num1 = int(input('좌변값을 하나 입력하세요'))
    num2 = int(input('우변값을 하나 입력하세요'))
    fmt = "%d + %d = %d \n %d - %d = %d \n"
    fmt += "%d * %d = %d \n %d + %d = %.5f \n"
    fmt += " %d ** %d = %d"
    print(fmt % (num1, num2, num1+num2, \
                 num1, num2, num1-num2, \
                 num1, num2, num1*num2, \
                 num1, num2, num1/num2, \
                 num1, num2, num1**num2 ))


#19윤년여부
def isLeapYear():
    year= int(
        input('윤년여부를 알고 싶은 년도를 입력하세요'))
    isLeap = '윤년이 아닙니다'

    if (( year % 4 == 0 and year % 100 != 0) or
          (year % 400 == 0)):
        isleap = '윤년입니다'

    print("%d는 %s" % (year, isleap))





#복권발행
def roulettetLotto():
    lotto = str(random.randint(100, 999))
    lucky = str(input('복권 숫자 3자리를 입력하세요\n'))
    match = 0 #일치여부
    prize = '꽝!!!!! 다음 기회에!'

    for i in [0,1,2]:
        for j in [0,1,2]:
            if (lucky[i] == lotto[j]):
                match +=1

    if match == 3:
        prize=('상금 1백만 지금')
    elif match == 2:
        prize=print('상금 1만 지급!')
    elif match == 1:
        prize= print ('상금 1천 지급')

    print(lucky,lotto, prize)

#성적데이터 클래스
class SungJukVO:
    def __init__(self, name, kor, eng, mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat
#성적처리용 클래스
class SungJukService:

    def getTotal(self,sj):
        tot = sj.kor + sj.eng + sj.mat
        return tot

    def getAverage(self,sj):
        avg = self.getTotal(sj) / 3
        return avg

    def getGrade(self,sj):
        grdlist = '가가가가가가미양우수수'
        var = int(self.getAverage(sj) / 10)
        grd = grdlist[var]  #자릿수, 자리위치값을 말해준다. var이 8이면 grdlist에서 8번째 자리에 있는 글자를 출력해준다
        return grd

sjsrv=SungJukService()
sj1 = SungJukVO('지현', 98, 45,23)
print(sj1.name)
print(sj1.kor)
print(sj1.eng)
print(sj1.mat)
print(sjsrv.getTotal(sj1))
print(sjsrv.getAverage(sj1))