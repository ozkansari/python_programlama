import degiskenler
from degiskenler import num1, lst1, str1

print('num1: ', degiskenler.num1)
print('lst1: ', degiskenler.lst1)
print('str1: ', degiskenler.str1)

degiskenler.num1 = 99
degiskenler.lst1[0] = 99
degiskenler.str1 = '99'

print('num1: ', degiskenler.num1)
print('lst1: ', degiskenler.lst1)
print('str1: ', degiskenler.str1)


print('num1: ', num1)
print('lst1: ', lst1)
print('str1: ', str1)
