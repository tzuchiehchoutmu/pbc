import math
from operator import length_hint
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
point =[]
point1 = [x1,y1]
point.append(point1)
point2 = [x2,y1]
point.append(point2)
point3 = [x1,y2]
point.append(point3)
point4 = [x2,y2]
point.append(point4)
length = []
def length_calculate(pointA,pointB) :
    x_dif = pointA[0] - pointB[0]
    y_dif = pointA[1] - pointB[1]
    line_length = math.sqrt(x_dif**2 + y_dif**2)
    return line_length
lineA = length_calculate(point1,point2)
length.append(lineA)
lineB = length_calculate(point1,point3)
length.append(lineB)
lineC = length_calculate(point4,point2)
length.append(lineC)
lineD = length_calculate(point4,point3)
length.append(lineD)
allsame = True
for line in length :
    if line != length :
        allsame = False
if allsame == False :
    print( "0"+" "+str(int(lineA*lineB)))
else:
    print( "1"+" "+str(int(lineA*lineB)))


