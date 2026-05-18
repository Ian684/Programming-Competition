from math import sqrt

def main():
    while True:
        try:
            num = int(input())
        except EOFError:break
        num = num*(num+1)//2
        c = sqrt(num)
        if c == int(c):
            print(int(c))
        else:
            print("null")

if __name__ == "__main__":
    main()
