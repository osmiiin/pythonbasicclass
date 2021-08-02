#class Candy:
#    def set_info(self, shape, color):
#        self.shape = shape
#        self.color = color

# satang = Candy()
# satang.set_info('circle', 'brown')

# print(satang.shape)
# print(satang.color)

#생성자
class Candy: # 더블언더바는 줄여서 던더라고 함
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

satang = Candy('circle', 'brown')

print(satang.shape)
print(satang.color)

#소멸자 : 사용되지 않음.
class Sample:
    def __del__(self):
        print('인스턴스가 소멸됩니다.')

sample = Sample()
del sample