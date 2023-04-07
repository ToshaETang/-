
n=int(input())
sand=[[0]*n]*n
for i in range (n):
    sand[i]=input().split(' ')

SAND=sand

for i in range (len(sand)):
    for j in range(len(sand[0])):
        if sand[i][j]=='2':
            sand[i][j]="■"
        elif sand[i][j]=='1':
            sand[i][j]="□" 
        else:
            print("wrong")

print("gravity off")

def putsand(X):
    for i in range(len(X)):
        print(X[i])

putsand(sand)

print("gravity on !")

for i in range (len(SAND)):
    for j in range(len(SAND[0])):
        if SAND[i][j]=="■":
            SAND[i][j]='2'
        elif SAND[i][j]=="□":
            SAND[i][j]='1'
        else:
            print("wrong")

for i in range (len(SAND)):
    for j in range(len(SAND[0])):
        SAND[i][j]=int(SAND[i][j])

for k in range (len(SAND)):
    for j in range (len(SAND[0])):
        for i in range (len(SAND)):
            if SAND[k][j]<SAND[i][j]:
                t=SAND[i][j]
                SAND[i][j]=SAND[k][j]
                SAND[k][j]=t

for i in range (len(SAND)):
    for j in range(len(SAND[0])):
        if SAND[i][j]==2:
            SAND[i][j]="■"
        elif SAND[i][j]==1:
            SAND[i][j]="□" 
        else:
            print("wrong")


putsand(SAND)









'''

