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

print("Задание 1")
#задание 1
x1 = rd.randint(0, 50)
y1 = rd.randint(0, 50)
z1 = rd.randint(0, 50)
print("A(", x1,",", y1, ",",z1, ");")

x2 = rd.randint(0, 50)
y2 = rd.randint(0, 50)
z2 = rd.randint(0, 50)
print("B(", x2, ",",y2, ",",z2, ");")

x3 = rd.randint(0, 50)
y3 = rd.randint(0, 50)
z3 = rd.randint(0, 50)
print("C(", x3,",", y3,",", z3, ").")

print()

#задание 2
print("Задание 2")
x4 = rd.randint(0, 50)
y4 = rd.randint(0, 50)
z4 = rd.randint(0, 50)

print("A(", x4,",", y4,",", z4, ");")

x5 = rd.randint(0, 50)
y5 = rd.randint(0, 50)
z5 = rd.randint(0, 50)

print("B(", x5,",", y5,",", z5, ").")
print();

#Задание 3
print("Задание 3")
isides = rd.randint(3, 4) #число сторон
if isides == 3: #треугольник
    #точка 1 фронтальная проекция
    xx1 = rd.randint(0,25)
    zz1 = rd.randint(0,25)
    # точка 2 фронтальная проекция
    xx2 = rd.randint(0,50)
    zz2 = rd.randint(0,25)
    #точка 3 фронтальная проекция
    xx3 = rd.randint(25,50)
    zz3 = rd.randint(25,50)
    # точка1 горизонтальная проекция
    yy1 = rd.randint(0, 50)
    yy2 = rd.randint(0, 50)
    yy3 = rd.randint(0, 50)

    xx = np.array([xx1, xx2, xx3, xx1])
    yy = np.array([yy1, yy2, yy3, yy1])
    zz = np.array([zz1, zz2, zz3, zz1])

elif isides == 4: #треугольник
    #точка 1 фронтальная проекция
    xx1 = rd.randint(0,25)
    zz1 = rd.randint(0,25)
    # точка 2 фронтальная проекция
    xx2 = rd.randint(0,25)
    zz2 = rd.randint(25,50)
    #точка 3 фронтальная проекция
    xx3 = rd.randint(25,50)
    zz3 = rd.randint(25,50)
    #точка 4 frontal
    xx4 = rd.randint(25,50)
    zz4 = rd.randint(0,25)

    # точка1 горизонтальная проекция
    yy1 = rd.randint(0, 25)
    yy2 = rd.randint(25, 50)
    yy3 = rd.randint(25, 50)
    yy4 = rd.randint(0, 25)

    xx = np.array([xx1, xx2, xx3, xx4, xx1])
    yy = np.array([yy1, yy2, yy3, yy4, yy1])
    zz = np.array([zz1, zz2, zz3, zz4, zz1])

elif isides == 5: #треугольник
    #точка 1 фронтальная проекция
    xx1 = rd.randint(0,16)
    zz1 = rd.randint(25,50)
    # точка 2 фронтальная проекция
    xx2 = rd.randint(16,33)
    zz2 = rd.randint(25,50)
    #точка 3 фронтальная проекция
    xx3 = rd.randint(33,50)
    zz3 = rd.randint(25,50)
    #точка 4 frontal
    xx4 = rd.randint(0,25)
    zz4 = rd.randint(0,25)
    #точка 5 frontal
    xx5 = rd.randint(25,50)
    zz5 = rd.randint(0,50)

    # точка1 горизонтальная проекция
    yy1 = rd.randint(25,50)
    yy2 = rd.randint(25,50)
    yy3 = rd.randint(25,50)
    yy4 = rd.randint(0, 50)
    yy5 = rd.randint(0, 50)

    xx = np.array([xx1, xx2, xx3, xx4, xx5, xx1])
    yy = np.array([yy1, yy2, yy3, yy4, yy5, yy1])
    zz = np.array([zz1, zz2, zz3, zz4, yy5, zz1])

elif isides == 6:
    #точка 1 фронтальная проекция
    xx1 = rd.randint(16,33)
    zz1 = rd.randint(36,50)
    # точка 2 фронтальная проекция
    xx2 = rd.randint(0,16)
    zz2 = rd.randint(24,36)
    #точка 3 фронтальная проекция
    xx3 = rd.randint(0,16)
    zz3 = rd.randint(12,24)
    #точка 4 frontal
    xx4 = rd.randint(16,33)
    zz4 = rd.randint(0,12)
    #точка 5 frontal
    xx5 = rd.randint(33,50)
    zz5 = rd.randint(12,24)
    #point7frontal
    xx6 = rd.randint(33, 50)
    zz6 = rd.randint(24, 36)

    # точка1 горизонтальная проекция
    yy1 = rd.randint(36,50)
    yy2 = rd.randint(24,36)
    yy3 = rd.randint(12,24)
    
    yy4 = rd.randint(0,12)
    yy5 = rd.randint(12,24)
    yy6 = rd.randint(24,36)

    xx = np.array([xx1, xx2, xx3, xx4, xx5, xx6, xx1])
    yy = np.array([yy1, yy2, yy3, yy4, yy5, yy6, yy1])
    zz = np.array([zz1, zz2, zz3, zz4, zz5, zz6, zz1])

var = rd.randint(1,3)
if var == 1:
    figure1 = plt.plot((0-xx), zz, "-")
    dots1 = plt.plot((0-xx), zz, "ro")
    figure2 = plt.plot((0-xx), (0-yy), "-")
    dots2 = plt.plot((0-xx), (0-yy), "ro")
elif var == 2:
    figure1 = plt.plot(yy, zz, "-")
    figure2 = plt.plot((0-xx), zz, "-")
    dots1 = plt.plot(yy, zz, "ro")
    dots2 = plt.plot((0-xx), zz, "ro")
elif var == 3:
    figure1 = plt.plot(yy, zz, "-")
    figure2 = plt.plot((0-xx), (0-yy), "-")
    dots1 = plt.plot(yy, zz, "ro")
    dots2 = plt.plot((0-xx), (0-yy), "ro")

xax = np.array([50,-50])
xyax = np.array([0, 0])
yax = np.array([50,-50])
yxax = np.array([0, 0])
xaxis = plt.plot(xax, xyax)
yaxis = plt.plot(yxax, yax)
plt.show()
