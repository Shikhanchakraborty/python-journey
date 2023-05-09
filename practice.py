#name="kakan@shikhan"
'''
print(type(name))

print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
print(name[1:9:2])
print(name[-5])
print(name[::-1])
print(name[-6::-1])
print(name[-14:])


print(name.swapcase())
print(name.count("an"))
print(name.find("x"))
print()

#type formaing
name="Shikhan"
age=25
roll=13
print("name : ",name,"Age : ",age,"roll: ",roll)
#print({"name : ",name,"Age : ",age,"roll: "})
'''
'''
class product:
    platform="Ali Baba"

    def __init__(self,title:str,price:float) -> None:
        self.title=title
        self.price=price

    def getDiscount(self)->float:
        return self.price*0.9


p1= product("Iphone-xr",29000)
print(p1.title)
print(p1.getDiscount())
'''
from turtle import*
goto(300,60)
pendown()
circle(40)
penup()
goto(-200,100)
goto(300,-140)
pendown()
circle(40)
penup()
goto(-200,-100)