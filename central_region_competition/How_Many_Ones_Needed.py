def count(n):
    i = 0
    c = 0
    n += 1
    while True:
        test = 2**i
        times = n // test
        if times == 0:
            break
        c += times // 2 * test
        if times & 1:
            c += n - times * test
        i += 1
    return c
def main():
    now = 0
    while True:
        a , b = map(int , input().split())
        if a == 0 and b == 0:break
        if a != 0:
            a = count(a-1)
        if b != 0:
            b = count(b)
        print(f"Case {now + 1} is {b-a}")
        now += 1

if __name__ == "__main__":
    main()
