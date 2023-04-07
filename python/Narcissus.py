for i in range(100,1000):
    g=(i%10)
    s=int((i/10))%10
    b=int(i/100)
    if (pow(g,3)+pow(s,3)+pow(b,3))==i:
        print(i)
     