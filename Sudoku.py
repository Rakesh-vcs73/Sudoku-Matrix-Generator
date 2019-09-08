#Program to generate 3x3 matrices with 3x3 elements as per the rules of SUDOKU.....
#Until now(In my system which is 32-bit)it only generated maximum 8 blocks where 9 blocks are required complete 3x3 matrices of 3x3 elements
#Program is complete when it prints "OOf All Matrices Generated----------------"
#Array arrangement of 9 arrays(a,b,c,d,e,f,g,h,i) in Sudoku puzzle 
#   a   b   c
#   d   e   f
#   g   h   i

import random
rows = 3
cols = 3

#to increase the number of recursions possible
#import sys
#print(sys.getrecursionlimit())
#sys.setrecursionlimit(1500)
#print(sys.getrecursionlimit())

a = [[0 for j in range(cols)] for k in range(rows)]
b = [[0 for j in range(cols)] for k in range(rows)]
c = [[0 for j in range(cols)] for k in range(rows)]
d = [[0 for j in range(cols)] for k in range(rows)]
e = [[0 for j in range(cols)] for k in range(rows)]
f = [[0 for j in range(cols)] for k in range(rows)]  
g = [[0 for j in range(cols)] for k in range(rows)]
h = [[0 for j in range(cols)] for k in range(rows)]
i = [[0 for j in range(cols)] for k in range(rows)]




def genRandom(a):
    BufferCount = 0
    for j in range(0,3):
        for k in range(0,3):
            num = random.randint(1,9)
            while((not CheckBlockRepeat(a,num)) or (CheckCheck(a,j,k,num))):
                #print("Check",num)
                num = random.randint(1,9)
                BufferCount+=1
                #print(BufferCount)
                if(BufferCount>50):
                    BufferCount=0
                    Restart()
                    j=0
                    k=0
                    genRandom(a)
                    #print('Cleared a------------------')
                    #print(a)
            a[j][k] = num
            #print(CheckBuffer)
            #print("Insert",a[j][k])
            

def CheckBlockRepeat(a,num):
    for j in range(0,3):
        for k in range(0,3):
            if(a[j][k]==num):
                return False
    return True


def CheckCheck(z,j,k,num):
    if(z==a):
        if((
        CheckRow(b,j,k,num) and
        CheckRow(c,j,k,num) and
        CheckCol(d,j,k,num) and
        CheckCol(g,j,k,num))):
            return False
    elif(z==b):
        if((
        CheckRow(a,j,k,num) and
        CheckRow(c,j,k,num) and
        CheckCol(e,j,k,num) and
        CheckCol(h,j,k,num))):
            return False
    elif(z==c):
        if((
        CheckRow(a,j,k,num) and
        CheckRow(b,j,k,num) and
        CheckCol(f,j,k,num) and
        CheckCol(i,j,k,num))):
            return False
    elif(z==d):
        if((
        CheckCol(a,j,k,num) and
        CheckCol(g,j,k,num) and
        CheckRow(e,j,k,num) and
        CheckRow(f,j,k,num))):
            return False
    elif(z==e):
        if((
        CheckCol(b,j,k,num) and
        CheckRow(d,j,k,num) and
        CheckRow(f,j,k,num) and
        CheckCol(h,j,k,num))):
            return False
    elif(z==f):
        if((
        CheckCol(c,j,k,num) and
        CheckCol(i,j,k,num) and
        CheckRow(d,j,k,num) and
        CheckRow(e,j,k,num))):
            return False
    elif(z==g):
        if((
        CheckCol(a,j,k,num) and
        CheckCol(d,j,k,num) and
        CheckRow(i,j,k,num) and
        CheckRow(h,j,k,num))):
            return False
    elif(z==h):
        if((
        CheckRow(g,j,k,num) and
        CheckCol(b,j,k,num) and
        CheckCol(e,j,k,num) and
        CheckRow(i,j,k,num))):
            return False
    else:
        if((
        CheckRow(g,j,k,num) and
        CheckCol(c,j,k,num) and
        CheckCol(f,j,k,num) and
        CheckRow(h,j,k,num))):
            return False
    return True




def CheckRow(a,j,k,num):
    for l in range(0,3):
        if(a[j][l]==num):
            return False
    return True


def CheckCol(a,j,k,num):
    for l in range(0,3):
        if(a[l][k]==num):
            return False
    return True

def show(a):
    for j in range(0,3):
        for k in range(0,3):
            print(a[j][k],end = " ")
        print()



def Restart():
    print("Restarted-------------------")
    for l in range(0,3):
        for m in range(0,3):
            a[l][m]=0
            b[l][m]=0
            c[l][m]=0
            d[l][m]=0
            e[l][m]=0
            f[l][m]=0
            g[l][m]=0
            h[l][m]=0
            i[l][m]=0
    genRandom(a)
    show(a)
    print()

    genRandom(b)
    show(b)
    print()

    genRandom(c)
    show(c)
    print()

    genRandom(d)
    show(d)
    print()

    genRandom(e)
    show(e)
    print()

    genRandom(f)
    show(f)
    print()

    genRandom(g)
    show(g)
    print()

    genRandom(h)
    show(h)
    print()

    genRandom(i)
    show(i)
    print()

    print('OOf All Matrices Generated----------------')
    

def start():
    genRandom(a)
    show(a)
    print()

    genRandom(b)
    show(b)
    print()

    genRandom(c)
    show(c)
    print()

    genRandom(d)
    show(d)
    print()

    genRandom(e)
    show(e)
    print()

    genRandom(f)
    show(f)
    print()

    genRandom(g)
    show(g)
    print()

    genRandom(h)
    show(h)
    print()

    genRandom(i)
    show(i)
    print()

    print('OOf All Matrices Generated----------------')

start()
    

