from math import tan, pi

def area_rPolygon(n, l):
    S = (n*l*l) / (4*tan(pi/n))
    return S

n = float(input("Input number of sides: "))
l = float(input("Input the length of a side: "))

print("The area of polygon is: " + str(area_rPolygon(n, l)))