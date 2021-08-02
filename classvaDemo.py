class Korean:
    
    country = '한국'

    @staticmethod
    def slogan():
        print('Imagine your Korea')

print(Korean.slogan())

# 클래스 변수 : 객체마다 서로 같은 값을 가지는 것
# 클래스 변수는 위에서 먼저 선언
# 객체 변수는 self키워드를 붙여 사용하지만 클래스 변수는 붙이는 것 없이 사용
 
    #def __init__(self, name, age, address):
    #    self.name = name
    #    self.age = age
    #    self.address = address

#    @classmethod
#    def trip(cls, country):
        if cls.country == country:
            print('국내여행입니다.')
        else:
            print('해외여행입니다.')

# print(Korean.trip('한국'))
# print(Korean.trip('미국'))

# man = Korean('홍길동', 35, '서울')
# woman = Korean('윤지영', 33, '경기')

# print(man.name)
# Korean.name

# 클래스 변수는 클래스, 객체 모두에 활용해서 갖다 쓸 수 있음
# print(man.country)
# print(Korean.country)

# print(woman.country)
#print(Korean.country)