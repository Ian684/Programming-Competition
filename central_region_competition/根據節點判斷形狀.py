from math import *

def get_points(line , check):
    points = []
    for l in line:
        for k , v in check.items():
            a , b = k
            if a <= l <= b:
                y = v * (sqrt(3) / 2)
                mid = (a + b) / 2
                x = l - mid
                points.append([x , y])
                break
    return points


def distance(i , j):
    return sqrt((i[0]-j[0])**2+(i[1]-j[1])**2)

def rt(line , check):
    points = get_points(line , check)
    dists = sorted([
        distance(points[0], points[1]),
        distance(points[1], points[2]),
        distance(points[2], points[0])
    ])
    return abs(dists[0] - dists[-1]) < 1e-4 and dists[0] > 1e-4

def rb(line , check):
    points = get_points(line , check)
    dists = []
    for i in range(4):
        for j in range(i+1, 4):
            dists.append(distance(points[i], points[j]))
    dists.sort()
    return abs(dists[0] - dists[3]) < 1e-4 and dists[0] > 1e-4


def rh(line , check):
    points = get_points(line , check)
    dists = []
    for i in range(6):
        for j in range(i+1, 6):
            dists.append(distance(points[i], points[j]))
    dists.sort()
    if dists[0] < 1e-4: return False
    return abs(dists[0] - dists[5]) < 1e-4 and abs(dists[6] - dists[11]) < 1e-4 and abs(dists[12] - dists[14]) < 1e-4

def main():
    check = {}
    l = 0
    i = 0
    a = 1
    while True:
        b = a + l
        check[(a , b)] = i
        i += 1
        l += 1
        a = b + 1
        if a > 500500:break
    while True:
        try:
            line = input().split()
        except EOFError:break
        if not line: continue
        aim = line[0]
        line = list(map(int , line[1:]))
        if aim == "Rhombus":
            if len(line) == 4 and rb(line , check):
                print("Yes")
            else:
                print("No")
        elif aim == "Regular_Hexagon":
            if len(line) == 6 and rh(line , check):
                print("Yes")
            else:
                print("No")
        elif aim == "Regular_Triangle":
            if len(line) == 3 and rt(line , check):
                print("Yes")
            else:
                print("No")
        else:
            print("No")
if __name__ == "__main__":
    main()
