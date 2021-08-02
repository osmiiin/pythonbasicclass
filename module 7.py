import time 
import datetime

print(time.time()) # 시간의 고유번호

print(time.ctime(time.time())) # 요일/월/일/시분초/연

print(time.strftime('%Y-%m-%d %a %H:%M:%S')) # 시간 서식 지정

print(time.sleep(1)) # 숫자(초)만큼 시스템 중지

present = datetime.datetime.now() # 마이크로초 단위까지 출력
print(present)

birthday = datetime.date(1990,8,31) # 특정 날짜 반환
print(birthday)

wake = datetime.time(10, 48, 0) # 특정 시간 반환
print(wake)

today = datetime.datetime.now() # 원하는 데이터만 추출
print(today.year)
print(today.month)
print(today.day)
print(today.hour)
print(today.minute)
print(today.second)

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1) # 날짜 및 시간 연산
tommorrow = today + datetime.timedelta(days=1)
print(yesterday)