#python 524.py

# 題目   https://buzzorange.com/techorange/2021/03/02/11-projects-for-python-beginner/
''' # 01. Odd or even
number = int(input("input a number"))

def Check(number):
    if number%2 == 0:
        print("偶數")
    else:
        print("奇數")

Check(number)
'''


'''# 02. Mad libs game
import random

list_v = []
while True:
    vocabulary = input("input a vocabular")
    if vocabulary == "0":
        break
    list_v.append(vocabulary)

list_s = []
def Mix(list_s):
    for i in range(len(list_v)):
        W = random.choice(list_v)
        list_s.append(W)
        list_v.remove(W)

    print(list_s)

Mix(list_s)
'''

'''# 03. Word count

Sentence = input("input a sentence  ")

print(str(len(Sentence.split())) + " words")
'''
