#python 4.19-2.py
class speed:
    def __init__(self, sl, avs, d):
        self.avs = avs/60
        self.sl = sl/60
        self.d = d
        self.time_saved = ((self.d)/(self.sl) - (self.d)/(self.avs))

A=speed(80, 90, 4000)
print(A.time_saved)