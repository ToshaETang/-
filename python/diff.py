#X^P-->

d=input("please input X,P")
d.split(',')
X=int(d[0])
P=int(d[2])


def p(A, B):
    if B==1 or B==0:
        return 1
    else:
        return A*p(A,B-1)


result=P*p(X,P)

print(X,"^",P,"  ","-->","  ",result )
