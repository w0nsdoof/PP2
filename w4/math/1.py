import math

def toRadian(degree:float):
    return float((math.pi * degree) / 180)

print("Output radian:", toRadian(float(input("Input degree: "))))



