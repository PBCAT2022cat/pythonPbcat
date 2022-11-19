import pygame,sys,time
from pygame.locals import *
from random import randint
pygame.init()

font = pygame.font.SysFont("arial",30)
def printwin(a,xy):
    aaa = font.render(a,True,(255,255,100))
    win.blit(aaa,xy)

class cell:
    def __init__(self,start):
        global sx,sy
        self.times = 0
        self.end = 0
        self.sc = (sx,sy)
        self.both = 5
        self.fire = 100000
        self.die = 5
        self.cells = []
        self.dies = ''
        a = []
        self.mostd = 6
        self.fired = 10
        self.die = 0
        for i in range(self.sc[0]):
            for x in range(self.sc[1]):
                if randint(0,start)==1:
                    b = 1
                else:
                    b = 0
                a.append([b,0,0])
            self.cells.append(a)
            a = []

    def upd(self):
        global mul
        alive = 0
        afire = 0
        
        for i in range(self.sc[0]):
            for x in range(self.sc[1]):
                if self.cells[i][x][0] == 1:
                    alive += 1
                if self.cells[i][x][1] == 1:
                    afire += 1
                
                    
                if randint(0,self.fire) == 1 and self.cells[i][x][0]==1 and i < self.sc[0]-10:#fire
                    self.cells[i][x][1] = 1
                    self.cells[i][x][2] = 1
                elif randint(0,self.die) == 1 and self.cells[i][x][0]==1:
                    self.cells[i][x][0] = 0
                    self.die += 1
                
                
                    
                    
                
                #######
                if randint(0,self.fired)==1:
                    self.cells[i][x][1]=0
                if self.cells[i][x][0] == 0:
                    self.cells[i][x] = [0,0,0]
                ii = i
                xx = x
                vellist,vel,nvel = [0,0,0,0,0,0,0,0],[],[]
                vellist[0],vellist[1] = (ii-1,xx),(ii+1,xx)
                vellist[2],vellist[3] = (ii,xx-1),(ii,xx+1)
                vellist[4],vellist[5] = (ii-1,xx-1),(ii+1,xx+1)
                vellist[6],vellist[7] = (ii-1,xx+1),(ii+1,xx-1)
                for aaa in vellist:
                    if self.cells[i][x][2] == 0 and self.cells[i][x][1] == 1:
                        try:
                            
                            if self.cells[aaa[0]][aaa[1]][1] != 1:
                                
                                self.cells[aaa[0]][aaa[1]][1] = 1
                                self.cells[aaa[0]][aaa[1]][2] = 1
                        except:
                            pass
                    try:
                        if self.cells[aaa[0]][aaa[1]][0] == 1:
                            vel.append(aaa)
                        else:
                            nvel.append(aaa)
                    except:pass
                if len(vel)<8 and randint(0,self.both)==1 and self.cells[i][x][1]==0:
                    try:
                        if self.cells[ii][xx][0]==1:
                            vellist = randint(0,len(nvel)-1)
                            vellist = nvel[vellist]
                            self.cells[vellist[0]][vellist[1]][0]=1
                    except:pass
                if len(vel)>self.most:
                    self.cells[i][x][0]=0
                    self.die += 1
                vellist = None
                vel = None
                nvel = None
                if self.cells[i][x][1] == 1 and self.cells[i][x][2]!=1:
                    self.cells[i][x] = [0,0,0]
                    self.die += 1
                
                #drw
                if self.cells[i][x][2] == 0 and self.cells[i][x][1] == 1:
                    pygame.draw.rect(win,(255,0,0),(i*mul,x*mul,1*mul,1*mul))
                elif self.cells[i][x][1] == 1:
                    pygame.draw.rect(win,(255,255,255),(i*mul,x*mul,1*mul,1*mul))
                elif self.cells[i][x][0] == 1:
                    pygame.draw.rect(win,(0,255,0),(i*mul,x*mul,1*mul,1*mul))
                    
                if self.cells[i][x][2] == 1:
                    self.cells[i][x][2] = 0
                elif self.cells[i][x][1] == 0:#fire die
                    self.cells[i][x][2]=0
                
                if self.die > 10000:
                    self.dies = self.dies+'|'
                    self.die = 0
        if alive != 0:
            self.times += 1
        printwin('alive:'+str(alive),(0,0))
        printwin(f'die{self.dies}:'+str(self.die),(0,200))
        printwin('fire:'+str(afire),(0,100))
        printwin('time:'+str(self.times),(200,0))
start = eval(input("start(1):"))
bth = eval(input("both(5):"))
die = eval(input("die(5):"))
fire = eval(input("fire(100000):"))
fired = eval(input("fireDie(10):"))
mostd = eval(input("most to die(6):"))

mul = eval(input("mul(10):"))
sx = eval(input("screen x(100):"))
sy = eval(input("screen y(80):"))
win = pygame.display.set_mode((sx*mul,sy*mul),0,32)
listc = cell(start)
listc.fire = fire
listc.both = bth
listc.die = die
listc.fired = fired
listc.most = mostd
while True:
    win.fill((0,0,0))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    listc.upd()
    pygame.display.update()







