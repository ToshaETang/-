# python 4.26-list-of-multiples.py

class list_of_multiples:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.list = []
        if self.b>0:
            for i in range (1,self.b+1):
               n = (self.a)*i
               self.list.append(n)
            self.list_of_multiples = self.list

        elif self.b==0:
            self.list_of_multiples = [0]
        
        else:
            for i in range (1,abs(self.b)+1):
               n = (self.a)*(-i)
               self.list.append(n)
            self.list_of_multiples = self.list

K=list_of_multiples(-6,3)

print(K.list_of_multiples)

