
# python Roulette.py
'''
import sys
if sys.version_info[0] == 2:
    import Tkinter
    from Tkinter import *
else:
    import tkinter as Tkinter
    from tkinter import *
import random

is_run = False


def lottery_whirl(data,i,number):
    global is_run
    if i == 0:
        j = 0
    else:
        j = i % 8
        data[j-1]['bg'] = '#CCCCCC'
        data[j]['bg'] = '#00CD00'
        wait = [a for a in range(100,300,10)] + [b for b in range(300,600,300 // (number-28))] + \
        [c for c in range(600,1200,120)] + [d for d in range(1200,1800,200)]
    if i < number:
        window.after(wait[i],lottery_whirl,data,i + 1,number)
    else:
        is_run = False


def lottery_start(data):
    global is_run
    if is_run:
        return
        is_run = True
    for x in range(len(data) - 1):
        data[x]['bg'] = '#CCCCCC'
        number = random.randint(30,53)
        lottery_whirl(data,number)


def create_label(name,x,y):
    label = Label(window,text=name,width=13,height=3,bg='#CCCCCC',font='宋體 -18 bold')
    label.place(anchor=NW,x=x,y=y)
    return label



if __name__ == '__main__':
    window = Tkinter.Tk()
    window.geometry('500x290+250+150')
    window.title(' 轉 盤 抽 獎 器')
    bg_label = Label(window,width=80,height=24,bg='#ECf5FF')
    bg_label.place(anchor=NW,x=0,y=0)

    label1 = create_label('風清揚',20,20)
    label2 = create_label('北丐',180,20)
    label3 = create_label('無崖子',340,20)
    label4 = create_label('西毒',20,110)
    label5 = create_label('東邪',340,110)
    label6 = create_label('掃地僧',20,200)
    label7 = create_label('南帝',180,200)
    label8 = create_label('張三丰',340,200)
    data = [label1,label2,label3,label5,label8,label7,label6,label4]
    button_core = Button(window,text='start', command=lambda:


lottery_start(data),width=130,height=53,bg='#00CD00',font='宋體 -18 bold',bitmap='gray50',compound=Tkinter.CENTER)
button_core.place(anchor=NW,x=180,y=110)

window.mainloop()
'''

import tkinter
# 匯入執行緒模組
import threading
import time

root = tkinter.Tk()
root.title('轉盤抽獎')
root.minsize(290,370)


# 擺放按鈕
btn1 = tkinter.Button(root, text = '1', bg = 'red')
btn1.place(x = 20, y = 20, width = 70, height = 70)

btn2 = tkinter.Button(root, text = '2', bg = 'white')
btn2.place(x = 110, y = 20, width = 70, height = 70)

btn3 = tkinter.Button(root, text = '3', bg = 'white')
btn3.place(x = 200, y = 20, width = 70, height = 70)

btn4 = tkinter.Button(root, text = '4', bg = 'white')
btn4.place(x = 20, y = 110, width = 70, height = 70)

btn5 = tkinter.Button(root, text = '5', bg = 'white')
btn5.place(x = 200, y = 110, width = 70, height = 70)

btn6 = tkinter.Button(root, text = '6', bg = 'white')
btn6.place(x = 20, y = 200, width = 70, height = 70)

btn7 = tkinter.Button(root, text = '7', bg = 'white')
btn7.place(x = 110, y = 200, width = 70, height = 70)

btn8 = tkinter.Button(root, text = '8', bg = 'white')
btn8.place(x = 200, y = 200, width = 70, height = 70)

# 將所有選項組成列表
prizelists = [btn1,btn2,btn3,btn5,btn8,btn7,btn6,btn4]

# 是否開啟迴圈的標誌
isloop = False
# 是否執行的標誌
functions = False

def round():
    # 判斷是否開始迴圈（防止多次按下開始按鈕程式開啟多次轉盤迴圈）
    if isloop == True:
        return

    # 初始化計數變數
    i = 0
    while True:
        # 延時操作
        time.sleep(0.00001)
        # 將所有元件的背景顏色變為白色
        for j in prizelists:
            j['bg'] = 'white'
        # 將當前數值對應的元件變色
        prizelists[i]['bg'] = 'red'

        i += 1
        # 如果i大於最大索引直接歸零
        if i >= len(prizelists):
            i = 0
        if functions == True:
            continue
        else:
            break

# 建立一個新執行緒的函式
def newtask():
    global isloop
    global functions
    # 建立執行緒
    t = threading.Thread(target = round)
    # 開啟執行緒執行
    t.start()
    # 設定迴圈開始標誌
    isloop = True
    # 是否執行的標誌
    functions = True

# 定義停止迴圈的函式
def stop():
    global isloop
    global functions

    functions = False
    isloop = False

# 開始按鈕
btn_start = tkinter.Button(root, text = '開始', command = newtask)
btn_start.place(x = 80, y = 300, width = 50, height = 50)

# 結束按鈕

btn_stop = tkinter.Button(root, text = '結束', command = stop)
btn_stop.place(x = 150, y = 300, width = 50, height = 50)

root.mainloop()