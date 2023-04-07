x1=int(input("X1"))
y1=int(input("y1"))
x2=int(input("X2"))
y2=int(input("y2"))
x3=int(input("x3"))
y3=int(input("y3"))
x4=int(input("x4"))
y4=int(input("y4"))


r=abs(x1*y2+x2*y3+x3*y4+x4*y1-x2*y1-x3*y2-x4*y3-x1*y4)/2
R=(abs(x1*y2-x2*y1)+abs(x2*y3-x3*y2)+abs(x3*y4-x4*y3)+abs(x4*y1-x1*y4))/2


if r==R:
    print("1")
else:
    print("0")



#class:屬性   方法(動作)
#建構子: 每個實體不會有一樣參數   

class Point():
    def_init_(self,x,y):
        self.x=X
        self.y=y

point_1=Point(1,4)