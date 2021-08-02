import math
import random

print(math.pi) # 원주율

print(math.ceil(1.1)) # 정수 올림

print(math.floor(1.9)) # 정수 내림

print(math.trunc(-1.9)) # 소수점 이하 삭제

print(math.floor(-1.9)) # 정수 내림(음수 일때는 그 아래 정수로)

print(math.sqrt(25)) # 제곱근(루트 25)

print(math.pow(2, 3)) # 제곱 -> a의 b승

print(random.randint(1, 10)) # 1 이상 10 이하의 정수

print(random.randrange(10)) # 0 이상 10미만의 정수
print(random.randrange(1, 10)) # 1 이상 10미만의 정수
print(random.randrange(1, 10, 2)) # 1 이상 10미만의 홀수

print(random.random()) # 0 이상 1 미만의 실수

if random.random() < 0.5:
    print("Hello")

seasons = ['spring', 'summer', 'fall', 'winter']
print(random.choice(seasons)) # 임의로 하나 선택해 산출

print(random.sample(range(1, 46), 6)) # range 범위 안에서 콤마 뒤 숫자만큼 임의의 수 산출

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list) # 임의의 순서로 재배치
print(my_list)