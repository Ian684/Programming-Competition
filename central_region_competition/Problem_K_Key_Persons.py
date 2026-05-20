from math import *

dfn = []
low = []
check = []
is_cut = []
timer = 0
primes = []

def generate_low(n , lines , u , parent):
    global dfn , low , check , is_cut , timer
    dfn[u] = timer
    low[u] = timer
    timer += 1
    check[u] = True
    children = 0
    for v in lines[u]:
        if not check[v]:
            children += 1
            generate_low(n , lines , v , u)
            low[u] = min(low[u] , low[v])
            if parent != -1 and low[v] >= dfn[u]:
                is_cut[u] = True
        elif check[v] and v != parent:
            low[u] = min(low[u] , dfn[v])
    if parent == -1 and children > 1:
        is_cut[u] = True


def main():
    global dfn , low , check , is_cut , timer
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = []
        lines = {}
        for j in range(n):
            lines[j] = set()
            a = int(input())
            for k in range(len(arr)):
                if gcd(arr[k] , a) != 1:
                    lines[j].add(k)
                    lines[k].add(j)
            arr.append(a)
        timer = 0
        dfn = [0]*n
        low = [0]*n
        check = [False]*n
        is_cut = [False]*n
        for s in range(n):
            if check[s]:continue
            generate_low(n , lines , s , -1)
        print(sum(is_cut))
if __name__ == "__main__":
    main()
