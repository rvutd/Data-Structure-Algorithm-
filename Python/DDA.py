# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

del_x = x2 - x1
del_y = y2 - y1

length = 0

if del_x > del_y:
    length = del_x
else:
    length = del_y

dx = del_x / length
dy = del_y / length

sign_del_x = 0
sign_del_y = 0

if del_x < 0:
    sign_del_x = -1
    
elif del_x == 0:
    sign_del_x = 0

elif del_x > 0:
    sign_del_x = 1
    
X = x1 + 0.5 * sign_del_x

if del_y < 0:
    sign_del_y = -1
    
elif del_y == 0:
    sign_del_y = 0

elif del_y > 0:
    sign_del_y = 1
    
Y = y1 + 0.5 * sign_del_y

i = 0
lst_x = []
lst_y = []

while (i <= length):
    X = X + del_x
    Y = Y + del_y
    lst_x.append(X)
    lst_y.append(Y)

    i = i + 1

print(X, Y)

    
plt.plot(lst_x, lst_y)
plt.show()

# import matplotlib.pyplot as plt

# # Getting Data
# x1 = int(input("x1 = "))
# x2 = int(input("x2 = "))
# y1 = int(input("y1 = "))
# y2 = int(input("y2 = "))

# # Getting values of del x & lenght:
# def del_values(x1, x2, y1, y2):
#     del_x = x2 - x1 
#     del_y = y2 - y1

#     if (del_x > del_y):
#         lenght = del_x
#     elif (del_y > del_x):
#         lenght = del_y

#     # Finding raster unit
#     raster_x = del_x/lenght 
#     raster_y = del_y/lenght
        
#     signx = signx_value(del_x)
#     signy = signx_value(del_y)

#     # Main Formula -
#     x = x1 + 0.5 * signx 
#     y = y1 + 0.5 * signy 

#     i = 0
#     while (i <= lenght):
#         x = x + raster_x
#         y = y + raster_y

#         lstx = []
#         lsty = []
#         lstx.append(x)
#         lsty.append(y)

#         i = i + 1

#         print(lstx, lsty)

#     plt.plot(lstx, lsty)
#     plt.show()

#     return print('x = ', x, 'y = ', y)


# def signx_value(del_x):
#     # Finding Sign X value
#     if del_x < 0:
#         signx = -1
#     elif del_x == 0:
#         signx = 0
#     elif del_x > 0:
#         signx = 1

#     return signx

# def signy_value(del_y):
# # Finding Sign Y value
#     if del_y < 0:
#         signy = -1
#     elif del_y == 0:
#         signy = 0
#     elif del_y > 0:
#         signy = 1

#     return signy

# del_values(x1,x2,y1,y2)

