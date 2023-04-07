#python 4.19-3.py
class mutipiy:
    def __init__(self, A):
        self.A = A
        self.list = []
        self.list_2 = []
        for i in range (len(self.A)):
            for j in range (len(self.A)):
                self.list.append(self.A[i])
            self.list_2.append(self.list)
            self.mutipiy = self.list_2
            self.list = []


K=mutipiy(["G","A","S","E"])

print(K.mutipiy)
