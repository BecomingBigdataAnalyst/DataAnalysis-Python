#딕셔너리 : 매핑 자료구조
#키에 값을 연결시키는 방식으로 데이터를 다루는 방법 제공
#키는 저장된 데이터를 식별하기 위한 번호나 이름
#값은 각 키에 연결되어 저장된 데이터
#따라서, 키만 알면 데이터를 바로 찾을 수 있음
#딕셔너리는 { } 에 키:값 형태로 이용
#키:값이 여러 개 존재 할 경우 , 로 구분

menu = {'1': 'newSungJuk', 2:'showSungJuk', 'abc':'modifySungJuk'}  #키는 다양한 자료형으로 사용

book = {
	'bookid': '1',
	'bookname' : '축구의역사' ,
	'publicher' : '굿스포츠',
	'price' : '7000',
    'orderdate' : '2014-07-01'
	}

order = {
    'orderid' : '1',
    'custid'  : '1',
    'bookid'  : '1',
    'saleprice' : '6000',
    'orderdate' : '2014-07-01'
}

customer={
    'custid' : '1',
    'bookid' : '1',
    'price'  : '7000',
    'orderdate' : '2014-07-01'
}


print(book)

books_list = []
books_list.append( book )
books_list.append( book )
books_list.append( book )

print(books_list)

#딕셔너리 처리 메서드
print('1' in book)      #딕셔너리에서 in 연산자는 key를 검색
print('bookid' in book)

print(book['bookid'])   #딕셔너리에서 키로 검색
print(book['bookname'])
print(book['price'])
#print(book['orderid'])  #존재하지 않는 키 검색시 오류!

print(book.get('bookname'))
print(book.get('orderid'))  #존재하지 않는 키 검색시 None 출력

bkname = book['bookname']   #키로 검색후 값 출력
print(bkname)

print(book.get('bookid'))
book['bookid'] = 99         #키로 값 수정
print(book.get('bookid'))

print(book)
book.update({'판형' : '3x4'}) #새로운 키 : 값 추가/ 수정
print(book)
book.update({":"})

print(book)
book.update({'판형' : '6 x 10'})  #새로운 키 : 값 수정
print(book)

del book['판형']                  #기존 키 삭제
print(book)

#book.clear()                   #모든 키 삭제

print(book.keys())              #모든 키를 출력
print(book.values())            #모든 값을 출력
print(book.items())             #모든 키: 값을 튜플로 출력
print(list(book.items()))             #모든 키 : 값을 튜플-리스트로 출력

items = book.items()            #모든 키: 값을 튜플 - 리스트로 출력
print(list(items))


abc=[1,2,3]
print(abc.reverse())






def myRange(start, end, hop=1) :
    retVal = start

    while retVal <= end:
        yield retVal
        retVal += hop
hap = 0
for i in myRange(1,5,2):      #종료값을 포함시킨 range 함수 작성
                            #결국, 리스트 형태의 값이 출력

#for i in range(1,5,2) :     #i : 1, 3
#for i in [1,3,5] :        # i : 1, 3, 5
    hap += i
print(hap)


def myRange2(start, end, hop=1) :
    retVal = start

    while retVal <= end:
        #return retVal ??       #중간 계산결과를 출력 또는 처리
        yield retVal            #실행중에 계싼된 값은
        retVal += hop           #generator 타입에 저장해 둠


myRange2(1,5,2)                 #yield로 넘긴 데이터는 순환형식의
a = myRange(1,5,2)              #generator 타입 생성


print(a)
print(next(a))                  #generator 타입에 저장된 값은
                                #iteator형식으로 다룰 수 있음
                                #iteator는 리스트에 저장된 객체를
                                #순환하며 하나씩 꺼내 사용하는 자료구조

print(next(a))
print(next(a))

for i in a:                     #generator 타입에 저장된 값은
        print(i)                #for문으로도 출력 가능