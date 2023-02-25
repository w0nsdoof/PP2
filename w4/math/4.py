def area_parallelogram(a, b):
    return a*b

length = int(input("Length of base: "))
height = int(input("Height of parallelogram: "))

area = area_parallelogram(length, height)

print(f"Area: {area}")

