#type formaing
'''
name="Shikhan"
age=25
height=13.56
print("name:",name,"Age:",age,"height:",height)

print("name:{0} age:{1} height: {2}".format(name,age,height))

print("name: %s age %d height %.2f "%(name,age,height))

print(f"name:{name} age:{age} height:{height:.1f}")

'''

'''
a=10
if a%2==0:
    print("Even number")
else:
    print("Odd number")
    '''

    #object orinted
'''
class product:
    platform = "SHARP"

    def __init__(self,title:str,price:int) -> None:
        self.title= title
        self.price=price
        self.discount=10

    def getDiscount(self)->float:
        return self.price*0.9


p1=product("Iphone",100000.0)
p2=product("Xioami",20000.0)
print(p1.title ,p1.price,p1.platform,p1.discount)
print(p2.title ,p2.price,p2.platform,p2.discount)
print(p1.getDiscount())
'''
''''
class product:
    platform="NOKIA"

    def __init__(self,title:str,price:int) -> None:
        self.title=title
        self.price=price
        self.__code=4565

    def getDiscount(self)->float:
        return self.price *0.9

    def getCode(self):
        return  self.__code

    


p1=product("Nokia 120",1200)
p2=product("Nokia 320",1300)

p1.title="Samsung"

print(p1.title,p1.price)
print(p2.title,p2.price)
print(p1.getDiscount())
print(p1.getCode())

'''
class product:
    platform="NOKIA"

    def __init__(self,title:str,price:int) -> None:
        self.title=title
        self.price=price
        self.__code=4565
# getter setter deleter
    @property 
    def code(self):
        print("is g etter")
        return self.__code

    @code.setter 
    def code(self,val):
        print("is setter")
        self.__code=val

    @code.deleter 
    def code(self):
        print("is deleter")
        del self.__code

p1=product("Nokia 120",1200)
p2=product("Nokia 320",1300) 
#print(p1.code)
p1.code=65456
print(p1.code)
print(p1.code)
