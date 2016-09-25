import os
import time

x = 0
y = 30-x
m = 1

a = input (" please input the cycle index :\n ")
s = int (a)
for i in range (s):
    m += 1
    if ( m % 60 < 30 ):
        x += 1
    else:
        x -= 1
    time.sleep (0.1)
    i = os.system ('cls')
    print (x * " " + "  *                        " + y * " ")  
    print (x * " " + "  *        *               " + y * " ")
    print (x * " " + "  *             *    *     " + y * " ")
    print (x * " " + "  *        *    *    *     " + y * " ")
    print (x * " " + "  *        *    *    *     " + y * " ")
    print (x * " " + "  ******   *     **** *    " + y * " ")