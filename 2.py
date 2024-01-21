# Python program explaining 
# save() function 
  
import numpy as geek
  
# a = geek.arange(9999999999)
a =[0] * 66566999
# a is printed.
print("a is:")
# print(a)
  
# the array is saved in the file geekfile.npy 
geek.save('geekfile', a)
  
print("the array is saved in the file geekfile.npy")