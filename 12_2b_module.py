import module2
from module2 import *

module2.x = 3

print('module2.x:', module2.x)
print('x:', x)

module2.y[0] = 3

print('module2.y:', module2.y)
print('y:', y)

# import * will not import _
# print('_z:', _z)
