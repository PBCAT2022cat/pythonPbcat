import random,sys,os

num = 0

do = [False,False,False,False]
canN = 0
past = []
val = []
place = []
canNum = 0
with open(sys.argv[1],'r') as file:
    vel = file.read()
    vel = vel.split('\n')
    for i in vel:
        place.append(i) 

def pasts(x,y):
    global past
    for i in past:
        if i[0] == y:
            if i[1] == x:
                return False
    return True
def pases(x,y):
    global pas
    if pas[0] == x:
        if pas[1] == y:
            return False
    return True

pas = (0,0)
x = 1
y = 1
vel = 0
val = 0
vx = 0
vy = 0
space = ' '
spac = [space,'*']

if place[x][y] != space:
    print('ERROR!x:1,y:1 必须是空格!')
    exit(-1)

for i in range(len(place)):
        if i == y:
            for ii in range(len(place[i])):
                if ii == x:
                    print('#',end='')
                else:
                    print(place[i][ii],end='')
            print()
        else:
            print(place[i])

while True:
    num += 1

    vx = x + 1
    if place[y][vx] in spac and pases(vx,y) and pasts(vx,y):#right
        do[3] = True
    else:
        do[3] = False
    
    vx = x - 1
    if place[y][vx] in spac and pases(vx,y) and pasts(vx,y):#left
        do[2] = True
    else:
        do[2] = False
    
    vy = y - 1
    if place[vy][x] in spac and pases(x,vy) and pasts(x,vy):#up
        do[0] = True
    else:
        do[0] = False
    
    vy = y + 1
    if place[vy][x] in spac and pases(x,vy) and pasts(x,vy):#down
        do[1] = True
    else:
        do[1] = False
    pas = (x,y)

    for i in do:
        if not i:
            canNum += 1
    if canNum == 4:############
        vx = x + 1
        if place[y][vx] in spac and pases(vx,y):#right
            do[3] = True
        else:
            do[3] = False
    
        vx = x - 1
        if place[y][vx] in spac and pases(vx,y):#left
            do[2] = True
        else:
            do[2] = False
    
        vy = y - 1
        if place[vy][x] in spac and pases(x,vy):#up
            do[0] = True
        else:
            do[0] = False
    
        vy = y + 1
        if place[vy][x] in spac and pases(x,vy):#down
            do[1] = True
        else:
            do[1] = False

    #----------------------
    canNum = 0
    for i in do:
        if not i:
            canNum += 1
    if canNum == 4:############
        vx = x + 1
        if place[y][vx] in spac:#right
            do[3] = True
        else:
            do[3] = False
        vx = x - 1
        if place[y][vx] in spac:#left
            do[2] = True
        else:
            do[2] = False
    
        vy = y - 1
        if place[vy][x] in spac:#up
            do[0] = True
        else:
            do[0] = False
    
        vy = y + 1
        if place[vy][x] in spac:#down
            do[1] = True
        else:
            do[1] = False
        #----------------------

        #######################
        
    
    while True:
        vel = random.randint(0,100)%4
        if do[vel]:
            break
    
    if vel == 0:
        y -= 1
    elif vel == 1:
        y += 1
    elif vel == 2:
        x -= 1
    elif vel == 3:
        x += 1

    if place[y][x] == '*':
        print(num)
        exit(num)

    for i in range(len(place)):
        if i == y:
            for ii in range(len(place[i])):
                if ii == x:
                    print('#',end='')
                else:
                    print(place[i][ii],end='')
            print()
        else:
            print(place[i])

    past.append((x,y))
    print(pas)



    

