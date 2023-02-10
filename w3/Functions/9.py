import math 

Radius = float(input())

def volume(r:float):
    return float((4*math.pi * (r**3)) / 3 )

print(volume(Radius))

