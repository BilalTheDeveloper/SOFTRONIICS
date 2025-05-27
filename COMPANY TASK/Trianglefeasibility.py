import math

sides = [4, 6, 3, 7] 

sides.sort(reverse=True)
max_area = 0

for i in range(len(sides) - 2):
    a, b, c = sides[i], sides[i+1], sides[i+2]
    if a < b + c:
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        max_area = area
        break

print(max_area)
