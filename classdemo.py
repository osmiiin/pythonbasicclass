class WaffleMachine:
    pass # 비워둘때는 pass로 표시(그냥 비워두면 안 될때 사용)

waffle = WaffleMachine()

print(waffle)
#%%
class Person:

    def who_am_i(self, name, age, tel, address): 
        self.name = name
        self.age = age
        self.tel = tel
        self.address = address

boy = Person()
girl = Person()

boy.who_am_i('john',15,'123-1234','toronto')
girl.who_am_i('alice',20,'321-4321','newyork')

print(boy.name)
print(boy.age)
print(boy.tel)
print(boy.address) # 16 오승민

print(girl.name)
print(girl.age)
print(girl.tel)
print(girl.address)