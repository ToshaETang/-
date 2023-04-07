# python 4.26_censor.py

# index  replace      self.a=self.a(' ')     "" 空字串    /////   : 才不會變數字    enumerate   break強制中斷迴圈

class Censor:
    def __init__(self,a,b,c):
        self.a = (a)
        self.b = (b)
        self.c = (c)

        #self.str_a_1 = (str(self.a)).split(' ')

     '''
        for i in range (len(self.b)):
            for j in range (len(self.str_a_1)):
                if self.str_a_1[j]==self.b[i]:
                    self.str_a_1[j]=self.c


        self.Censor = self.str_a_1
'''


K=Censor(["The cow jumped over the moon."], ["cow", "over"], ["*"])

print(K.Censor)