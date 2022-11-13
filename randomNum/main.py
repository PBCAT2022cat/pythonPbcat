import random,sys,os,time
import random
import os,random
import time,sys,pygame,tkinter
import colorama
colorama.init(True)
def red (a):
    print("\033[31m"+a+"\033[0m")
print("\033[31m-----\033[0m")
print("\033[31m---------------run------------------\033[0m")

def signOn(a=[],b=[]):
    if a[0] == b[0]:
        if a[1] == b[1]:
            return True
    return False
red('sign on')
val = input("""
name:""" )
vel = input('password:')
file = open('./signOn.txt','r')
dd = file.readlines()
for i in dd:
    bb = i.strip('\n')
    bb = bb.split(' ')
    if signOn(bb,[val,vel]):
        break
    else:
        red('password or name error!')
        os.system('PAUSE')
        sys.exit()
    

red("random num game!")

cout=''
vel = ''
hai = ''
p1 = ''
p2 = ''

while True:
    red('''
0 quit game
1 play game
2 good time
3 clean all good time
4 data
5 sign in
6 setting

''')
    cout = input('''
do:''')

    if cout == '1':
        red("game start...")
        p1 = input("name:")


        while True:
            pass
            
        
    

    
