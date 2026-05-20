from math import *

def main():
    while True:
        try:
            n = int(input())
        except EOFError:break
        valid = True
        if n <= 0:
            valid = False
        if valid:
            total = set()
            for i in range(2 , int(sqrt(n))+1):
                if n % i == 0:
                    total.add(i)
                    total.add(n//i)
            if sum(total)+1 != n:
                valid = False
        if valid:
            print(f"{n} is a perfect number")
        else:
            print(f"{n} is not a perfect number")

if __name__ == "__main__":
    main()
