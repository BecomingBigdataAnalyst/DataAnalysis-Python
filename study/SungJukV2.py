#총점 getTotal()
#평균 getAverage()
#함수 getGrade
# 성적 처리프로그램 V1
# 이름name, 국어 kor, 영어eng, 수학mat
# 총점 tot, 평균 avg, 학점grd



def getTotal():
    #pass   #dummy code
    tot = kor + eng + mat
    return tot

def getAverage():
   avg=getTotal()/3
   return avg

def getGrade():
   avg = getAverage()
   grd = '가'
   if avg >= 90:
       grd = '수'
   elif avg >= 80:
       grd = '우'
   elif avg >= 70:
       grd = '미'
   elif avg >= 60:
       grd = '양'
   return grd

print('-- 성적 처리 프로그램 v2 --')

name = input('이름을 입력하세요 ')
kor = int(input('국어 점수를 입력하세요 '))
eng = int(input('영어 점수를 입력하세요 '))
mat = int(input('수학 점수를 입력하세요 '))

fmt = '%s %d %d %d %d %.2f %s'

print(fmt % (name, kor, eng, mat,
             getTotal(), getAverage(), getGrade()))
