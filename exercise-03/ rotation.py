import os
import time
import copy

a = ['a1','a2','a3','a4','a5','a6','a7','a8']
a[0] = "   **   "
a[1] = "  *  *  "
a[2] = " *    * "
a[3] = "*  **  *"
a[4] =a[5] = a[6] = a[7] = a[0]##可以任意的设定想要的图案

l = [[' ' for col in range(8)] for row in range(8)]
lx = copy.deepcopy(l)

for i in range (0,8):
    l[i] = list (a[i])
    
s = int(input("please input the cycle index :\n")) 

for i in range (s):
    time.sleep (0.1)
    i = os.system ('cls')
    print (a[0])
    print (a[1])
    print (a[2])
    print (a[3])
    print (a[4])
    print (a[5])
    print (a[6])
    print (a[7])##输出图像
    for m in range (0,8):
        for n in range (0,8):
            lx[m][n] = l[7-n][m]
    l = copy.deepcopy(lx)##做九十度的顺时针旋转
    for j in range (0,8):
        a[j] = "".join(l[j])         
   
   
        
    
        
    
    



