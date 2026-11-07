import math

x1 = float(input("entre x1:"))
x2 = float(input("entre x2:"))

y1 = float(input("entre y1:"))
y2 = float(input("entre y2:"))

distance = math.sqrt((x2 - x1)**2 + (y2-y1)**2)

print("euclidean distance",distance)