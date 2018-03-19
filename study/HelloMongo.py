#-*- coding: utf-8 -*-
from pymongo import MongoClient
import pprint
import datetime

#MongoDB에 외부접속을 허용 하려면
#설정파일에 'bind_ip=아이피주소'를 추가

#몽고비디 연결객체 만들기
#client = MongoClient() #내부에서 접속하는거면 이렇게!
#client = MongoClient('192.168.56.102',27017) #외부에서 접속하는거면 이렇게 써줘야한다
client = MongoClient('mongodb://192.168.56.102:27017')

#데이터베이스 객체 가져오기
#db = client['zzyzzy']
db = client.zzyzzy

#컬렉션 객체 가져오기
#coll = db['inventory']
coll = db.inventory
coll2 = db.inventory2
coll3 = db.restaurants

#단일문서 조회
#print(coll.find_one())
#print(coll2.find_one())


#단일문서 조회 - JSON을 보기좋게 출력하기 (pprint)
print(coll.find_one())

#전체문서 조회(커서를 이용해야 함)
pprint.pprint(coll.find())
cursor = coll.find()
for doc in cursor:
    pprint.pprint(doc)

cursor = coll2.find({})
for doc in cursor:
    pprint.pprint(doc)

cursor = coll3.find({})
for doc in cursor:
    pprint.pprint(doc)

#cursor = coll3.find({})
#for doc in cursor:
#    pprint.pprint(doc)

#조건으로 질의하기
#item이 notebook
print(coll.find_one({'item':'notebook'}))

#qty가 50보다 작은 item 조회
print(coll2.find_one({'qty':{"$lte": 50} }))
#우편번호가 10075인 음식점 조회
print(coll3.find_one({'zipcord':'10462'}))

cursor = coll.find({'item':'notebook'})
for doc in cursor:
    print(doc)
cursor = coll2.find({'qty':{"$lte": 50} })
for doc in cursor:
    print(doc)

cursor = coll3.find({'zipcode.address':'10462'})
for doc in cursor:
    print(doc)

#데이터 추가하기 - JSON생성
student = {'hakbun':'a12345',
           'name':'혜교',
           'addr':'seoul, korea',
           'regdate':datetime.datetime.now()}

#데이터 추가하고 생성된 object_id 값을 objId 변수에 저장
objId = db.students.insert_one(student)
print(objId)
print(db.students.find_one())
many_student = [{'hakbun':'a98765',
                'name':'지현',
                'addr':'pusan, korea',
                'regdate':datetime.datetime.now() },
                {'hakbun': 'x24680',
                'name': '수지',
                'addr': 'daejeon, korea',
                'regdate': datetime.datetime.now() }]

result = db.students.insert_many(many_student)
print(result.inserted_ids)

#데이터 수정
#학번 a12345인 학생의 주소를 인천으로 변경
result = db.students.update_one({'hakbun':'a12345'},{"$set":{'addr':'incheon,korea'}})
print(result.matched_count,result.modified_count)

result = db.students.update_many(
    {'hakbun':'a12345'},
    {"$set":{'addr':'incheon,korea'}})
print(result.matched_count,result.modified_count)

#데이터 삭제
#학번 a12345인 학생 정보 삭제
result = db.students.delete_one({'hakbun':'a12345'})
print(result.deleted_count)

result = db.students.delete_many({'hakbun':'a12345'})
print(result.deleted_count)

result = db.students.delete_one({})  #모두 삭제
print(result.deleted_count)

#몽고디비 접속해제
client.close()






