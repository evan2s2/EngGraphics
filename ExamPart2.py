import random as rd
import numpy as np
import matplotlib.pyplot as plt

#plot settings
fig, ax = plt.subplots()
ax.set_xlim(-60,60)
ax.set_ylim(-60,60)
xaxis = np.array([-50,50]); zeros = np.array([0,0]); yaxis = np.array([-50,50]); xax = plt.plot(xaxis, zeros, "-"); yax = plt.plot(zeros, yaxis, "-")
fig.set_figwidth(5)
fig.set_figheight(5)
plt.xticks([])
plt.yticks([])
ax.set_yticklabels([])
ax.set_xticklabels([])

################### CONE #####################################################
def conefrontal():
    #конус
    #frontal projection
    xf1 = np.array([-18, -24, -12, -18])
    yf1 = np.array([40, 5, 5, 40])
    frontal = plt.plot(xf1, yf1)
def coneprofile():
    #profile projection
    xp = np.array([18, 24, 12, 18])
    yp = np.array([40, 5, 5, 40])
    profile = plt.plot(xp, yp)
def conehorizontal():
    #horizontal projection
    horizontal = plt.Circle((-18,-18), 6, fill = False)
    fig = plt.gcf()
    ax.add_artist(horizontal)
    circlecenter = plt.plot(-18,-18, "ro")
def cone():
    rndcone = rd.randint(1,3)
    if rndcone == 1:
        conefrontal()
        conehorizontal()
    elif rndcone == 2:
        conefrontal()
        coneprofile()
    elif rndcone == 3:
        conehorizontal()
        coneprofile()
    plt.show()
##########################################################################

###################### лавочка ###########################################
def bench():
    #direct coordinates
    x1 = 40; y1 = 40; z1 = 30
    x2 = 40; y2 = 40; z2 = 10
    x3 = 10; y3 = 40; z3 = 10
    x4 = 10; y4 = 40; z4 = 40
    x5 = 25; y5 = 40; z5 = 40
    x6 = 25; y6 = 40; z6 = 30
    x7 = 40; y7 = 10; z7 = 30
    x8 = 40; y8 = 10; z8 = 10
    x9 = 10; y9 = 10; z9 = 10
    x10 = 10; y10 = 10; z10 = 40
    x11 = 25; y11 = 10; z11 = 40
    x12 = 25; y12 = 10; z12 = 30
    #frontal projection
    xf = np.array([x1, x2, x3, x4, x5, x6, x1])
    yf = np.array([z1, z2, z3, z4, z5, z6, z1])
    #horizontal
    xh = np.array([x5, x1, x7, x11, x10, x4, x5, x11])
    yh = np.array([y5, y1, y7, y11, y10, y4, y5, y11])
    #profile
    xp = np.array([y1, y2, y8, y7, y11, y5, y1, y7])
    yp = np.array([z1, z2, z8, z7, z11, z5, z1, z7])
    a = np.array([[xf, yf] , [xh, yh], [xp, yp]])
    return a

def eightgrain():
    x1 = 40; y1 = 20; z1 = 45
    x2 = 45; y2 = 20; z2 = 40
    x3 = 45; y3 = 20; z3 = 10
    x4 = 40; y4 = 20; z4 = 5
    x5 = 10; y5 = 20; z5 = 5
    x6 = 5; y6 = 20; z6 = 10
    x7 = 5; y7 = 20; z7 = 40
    x8 = 10; y8 = 20; z8 = 45
    x9 = 40; y9 = 10; z9 = 45
    x10 = 45; y10 = 10; z10 = 40
    x11 = 45; y11 = 10; z11 = 10
    x12 = 40; y12 = 10; z12 = 5
    x13 = 10; y12 = 10; z13 = 5
    x14 = 5; y14 = 10; z14 = 10
    x15 = 5; y15 = 10; z15 = 40
    x16 = 10; y16 = 10; z16 = 45
    #frontal
    xf = np.array([x1, x2, x3, x4, x5, x6, x7, x8, x1])
    yf = np.array([z1, z2, z3, z4, z5, z6, z7, z8, z1])
    #horizontal
    xh = np.array([x2, x1, x8, x7, x15, x16, x8, x16, x9, x1, x9, x10, x2])
    yh = np.array([y2, y1, y8, y7, y15, y16, y8, y16, y9, y1, y9, y10, y2])
    #profile
    xp = np.array([y1, y2, y3, y4, y12, y11, y3, y11, y10, y2, y10, y9, y1])
    yp = np.array([z1, z2, z3, z4, z12, z11, z3, z11, z10, z2, z10, z9, z1])
    a = np.array([[xf, yf] , [xh, yh], [xp, yp]])
    return a

def star():
    a1 = np.array([-9+15,2+15, 10])
    a2 = np.array([-3+15,3+15, 10])
    a3 = np.array([0+15,8+15, 10])
    a4 = np.array([3+15,3+15, 10])
    a5 = np.array([9+15,2+15, 10])
    a6 = np.array([5+15,-3+15, 10])
    a7 = np.array([6+15,-9+15, 10])
    a8 = np.array([0+15,-7+15, 10])
    a9 = np.array([-6+15,-9+15, 10])
    a10 = np.array([-5+15,-3+15, 10])
    a11 = np.array([-9+15,2+15, 10])
    #frontal
    xf = np.array([ a1[0], a2[0],a3[0],a4[0],a5[0],a6[0],a7[0],a8[0],a9[0], a10[0], a11[0] ])
    yf = np.array([ a1[2], a2[2],a3[2],a4[2],a5[2],a6[2],a7[2],a8[2],a9[2], a10[2], a11[2] ])
    #horizontal
    xh = np.array([ a1[0], a2[0],a3[0],a4[0],a5[0],a6[0],a7[0],a8[0],a9[0], a10[0], a11[0] ])
    yh = np.array([ a1[1], a1[1],a3[1],a4[1],a5[1],a6[1],a7[1],a8[1],a9[1], a10[1], a11[1] ])
    #profile
    xp = np.array([ a1[1], a1[1],a3[1],a4[1],a5[1],a6[1],a7[1],a8[1],a9[1], a10[1], a11[1] ])
    yp = np.array([ a1[2], a2[2],a3[2],a4[2],a5[2],a6[2],a7[2],a8[2],a9[2], a10[2], a11[2] ])
    a = np.array([[xf, yf] , [xh, yh], [xp, yp]])*2
    return a

def house():
    a1 = np.array([40, 10, 20])
    a2 = np.array([40, 40, 20])
    a3 = np.array([5, 40, 20])
    a4 = np.array([5, 10, 20])
    a5 = np.array([40, 10, 5])
    a6 = np.array([40, 40, 5])
    a7 = np.array([5, 40, 5])
    a8 = np.array([5 ,10, 5])
    a9 = np.array([40, 25, 40])
    a10 = np.array([5, 25, 40])
    #frontal
    xf = np.array([ a6[0], a2[0], a9[0], a10[0], a3[0], a2[0], a3[0], a7[0], a6[0] ])
    yf = np.array([ a6[2], a2[2], a9[2], a10[2], a3[2], a2[2], a3[2], a7[2], a6[2] ])
    #horiz
    xh = np.array([ a1[0], a9[0], a2[0], a3[0], a10[0], a9[0], a10[0], a4[0], a1[0] ])
    yh = np.array([ a1[1], a9[1], a2[1], a3[1], a10[1], a9[1], a10[1], a4[1], a1[1] ])
    #profile
    xp = np.array([ a1[1], a9[1], a2[1], a1[1], a2[1], a6[1], a5[1], a1[1] ])
    yp = np.array([ a1[2], a9[2], a2[2], a1[2], a2[2], a6[2], a5[2], a1[2] ])
    a = np.array([[xf, yf] , [xh, yh], [xp, yp]])
    return a

def airplane():
    a1 = np.array([9+10, 0+10, 10])
    a2 = np.array([10+10, 1+10, 10])
    a3 = np.array([10+10, 5+10, 10])
    a4 = np.array([9+10, 5+10, 10])
    a5 = np.array([7+10, 2+10, 10])
    a6 = np.array([-5+10, 2+10, 10])
    a7 = np.array([-7+10, 0+10, 10])
    a8 = np.array([9+10, 0+10, 10])
    a9 = np.array([0+10, 2+10, 10])
    a10 = np.array([5+10, 6+10, 10])
    a11 = np.array([7+10, 6+10, 10])
    a12 = np.array([4+10, 2+10, 10])
    a13 = np.array([0+10, 1+10, 10])
    a14 = np.array([4+10, 1+10, 10])
    a15 = np.array([8+10, -3+10, 10])
    a16 = np.array([6+10, -3+10, 10])
    a17 = np.array([0+10, 1+10, 10])
    #frontal
    xf = np.array([ a1[0], a2[0],a3[0],a4[0],a5[0],a6[0],a7[0],a8[0],a9[0], a10[0], a11[0], a12[0], a13[0], a14[0], a15[0], a16[0], a17[0] ])*2
    yf = np.array([ a1[2], a2[2],a3[2],a4[2],a5[2],a6[2],a7[2],a8[2],a9[2], a10[2], a11[2], a12[2], a13[2], a14[2], a15[2], a16[2], a17[2] ])*2
    #horizontal
    xh = np.array([ a1[0], a2[0],a3[0],a4[0],a5[0],a6[0],a7[0],a8[0],a9[0], a10[0], a11[0], a12[0], a13[0], a14[0], a15[0], a16[0], a17[0] ])*2
    yh = np.array([ a1[1], a1[1],a3[1],a4[1],a5[1],a6[1],a7[1],a8[1],a9[1], a10[1], a11[1], a12[1], a13[1], a14[1], a15[1], a16[1], a17[1]])*-2 + 50
    #profile
    xp = np.array([ a1[1], a1[1],a3[1],a4[1],a5[1],a6[1],a7[1],a8[1],a9[1], a10[1], a11[1], a12[1], a13[1], a14[1], a15[1], a16[1], a17[1] ])*2
    yp = np.array([ a1[2], a2[2],a3[2],a4[2],a5[2],a6[2],a7[2],a8[2],a9[2], a10[2], a11[2], a12[2], a13[2], a14[2], a15[2], a16[2], a17[2] ])*2
    a = np.array([[xf, yf] , [xh, yh], [xp, yp]])
    return a

def pyramid():
    #points
    a1 = np.array([25,25,5])
    a2 = np.array([35,15,5])
    a3 = np.array([15,15,5])
    a4 = np.array([(rd.randint(22,28)),20,40])
    #projections
    xf = np.array([ a2[0], a1[0], a3[0], a4[0], a1[0], a4[0], a2[0] ])
    yf = np.array([ a2[2], a1[2], a3[2], a4[2], a1[2], a4[2], a2[2] ])
    xh = np.array([ a1[0], a2[0], a3[0], a1[0], a4[0], a3[0], a4[0], a2[0] ])
    yh = np.array([ a1[1], a2[1], a3[1], a1[1], a4[1], a3[1], a4[1], a2[1] ])
    xp = np.array([ a2[1], a1[1], a4[1], a2[1] ])
    yp = np.array([ a2[2], a1[2], a4[2], a2[2] ])
    a = np.array([[xf, yf] , [xh, yh], [xp, yp]])
    return a

######### CYLINDER ######################################################################
r = rd.randint(10,20)
x = rd.randint(20,25)
y = rd.randint(20,25)
zup = rd.randint(30,35)
zdown = rd.randint(5,10)

def cylinderfrontal():
    #frontal projection
    xf = np.array([ 0-x-r, 0-x+r, 0-x+r, 0-x-r, 0-x-r ])
    yf = np.array([ zup, zup, zdown, zdown, zup])
    frontal = plt.plot(xf, yf)
def cylinderprofile():
    #profile projection
    xp = np.array([ y-r, y+r, y+r, y-r, y-r ])
    yp = np.array([ zup, zup, zdown, zdown, zup ])
    profile = plt.plot(xp, yp)
def cylinderhorizontal():
    #horizontal projection
    horizontal = plt.Circle((-x,-y), r, fill = False)
    fig = plt.gcf()
    ax.add_artist(horizontal)
def cylinderplot():
    rndcylinder = rd.randint(1,2)
    if rndcylinder == 1:
        cylinderfrontal()
        cylinderhorizontal()
    elif rndcylinder == 2:
        cylinderhorizontal()
        cylinderprofile()
    plt.show()
################################################################################
def rnd(a):
    rnd = rd.randint(1,2)
    if rnd == 1:
        frontal = plt.plot(0 - a[0][0], a[0][1], "-")
        horizontal = plt.plot(0 - a[1][0], 0 - a[1][1], "-")
    elif rnd == 2:
        horizontal = plt.plot(0 - a[1][0], 0 - a[1][1])
        profile = plt.plot(a[2][0], a[2][1])
    plt.show()
##################     FINAL VAR RANDOMIZING   #################################
var =  rd.randint(1,8)
if var == 1:
    rnd(bench())
elif var == 2:
    cone()
elif var == 3:
    rnd(eightgrain())
elif var == 4:
    rnd(star())
elif var == 5:
    rnd(house())
elif var == 6:
    rnd(airplane())
elif var == 7:
    rnd(pyramid())
elif var == 8:
    cylinderplot()
################################################################################
