file = open('오승민.txt', 'rt')

while True:
    str = file.read(5)
    if not str:
        break
    print(str, end='')
file.close()

#주말숙제
#1 잡스 영화보기
#2 점프투파이썬 4장까지
#3 일일숙제