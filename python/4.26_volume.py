# python 4.26_volume.py

class volume:
    def __init__(self,R,r):
        self.R = R
        self.r = r
        self.volume = (4*3.14*abs(pow(self.R,3)-pow(self.r,3)))/3

vol_shell=volume(7,2)

print(vol_shell.volume)
