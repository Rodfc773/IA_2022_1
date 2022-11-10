import math
import pandas as pd


x = float(input())
y = float(input())
z = float(input())

total = x + y + z

if x != 0 and y != 0 and z != 0:
                gain += (mydict[key] * (x*math.log2(x) + y*math.log2(y) + z*math.log2(z)))/14
Entrophy = -1 * ((((x) * math.log2(x) ) + ((y) * math.log2( y)) + ((z) * math.log2(z)))/total)

print("Resultado da Entropia(S): {}".format(Entrophy))
