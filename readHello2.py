file = open('오승민.txt', 'rt')

while True:
    str = file.read(5)
    if not str:
        break
    print(str, end='')
file.close()