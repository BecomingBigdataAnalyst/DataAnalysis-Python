#성적 처리프로그램 V3
#이름name, 국어kor, 영어eng, 수학mat
#총점 tot, 평균avg, 학점grd
#getTotal, getAverage, getGrade
#리스트 자료구조를 이용한다.

def grade_list(avg):
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

name_list=[]
kor_list=[]
eng_list=[]
mat_list=[]

tot_list=[]
avg_list=[]
grd_list=[]

print('--성적 처리 프로그램V3--')

#name=input('이름을 입력하세요')
#name_list.append(name)
while True:
    idx = len(name_list)    #인덱스 지정
    
    name_list.append(input('이름을 입력하세요'))
    kor_list.append(int(input('국어점수를 입력하세요')))
    eng_list.append(int(input('영어점수를 입력하세요')))
    mat_list.append(int(input('수학점수를 입력하세요')))

    tot_list.append(kor_list[idx] + eng_list[idx] + mat_list[idx])
    avg_list.append(tot_list[idx]/3)
    grd_list.append(grade_list(avg_list[0]))
    #grd_list.append('가')


    fmt = '%s %d %d %d %d %.2f %s'
    print( fmt % (name_list[idx], kor_list[idx], eng_list[idx],\
                mat_list[idx], tot_list[idx], avg_list[idx],
                grd_list[idx]))
    
    is_exit = input('계속 하시겠습니까? (y/n)')
    if is_exit == 'n':
        idx +=1
        print(idx,'명의 학생 처리했습니다')
        break
