def cross(a , b):
    return a[0]*b[1]-a[1]*b[0]

def isclock(need_equal , a , b , c):
    p = [b[0]-a[0] , b[1]-a[1]]
    q = [c[0]-a[0] , c[1]-a[1]]
    if need_equal:
        if cross(p , q) <= 0:return True
    else:
        if cross(p , q) < 0:return True
    return False

def generate_poly(poly):
    if len(poly) <= 2:
        return poly
    u = [poly[0] , poly[1]]
    for i in range(2 , len(poly)):
        while len(u) >= 2 and not isclock(False , u[-2] , u[-1] , poly[i]):
            u.pop()
        u.append(poly[i])
    l = [poly[-1] , poly[-2]]
    for i in range(len(poly)-3 , -1 , -1):
        while len(l) >= 2 and not isclock(False , l[-2] , l[-1] , poly[i]):
            l.pop()
        l.append(poly[i])
    for i in range(1 , len(u)-1):
        l.append(u[i])
    return l

def solve(cops , robbers , aim):

    safe , robbed = True , True
    cops = sorted(cops)
    cops = generate_poly(cops)
    if len(cops) <= 2:
        cops = []
        safe = False
    robbers = sorted(robbers)
    robbers = generate_poly(robbers)
    if len(robbers) <= 2:
        robbers = []
        robbed = False

    for i in range(len(cops)):
        j = (i+1)%len(cops)
        if not isclock(True , cops[i] , cops[j] , aim):
            safe = False
            break

    for i in range(len(robbers)):
        j = (i+1)%len(robbers)
        if not isclock(True , robbers[i] , robbers[j] , aim):
            robbed = False
            break

    if safe:
        return "safe"
    if robbed:
        return "robbed"
    return "neither"

def main():
    now = 0
    while True:
        cop , robber , citizen = map(int , input().split())
        if cop == 0 and robber == 0 and citizen == 0:break
        cops , robbers = [] , []
        for i in range(cop):
            cops.append(list(map(int , input().split())))
        for i in range(robber):
            robbers.append(list(map(int , input().split())))
        print(f"Data set {now+1}:")
        now += 1
        for i in range(citizen):
            aim = list(map(int , input().split()))
            status = solve(cops , robbers , aim)
            print(f"     Citizen at ({aim[0]},{aim[1]}) is {status}.")
        blank_line = input()
        print()

if __name__ == "__main__":
    main()
