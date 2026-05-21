def main():
    alph = set()
    for i in range(26):
        alph.add(chr(i+65))
        alph.add(chr(i+97))
    while True:
        try:
            line = input().split()
            if len(line) != 2:
                print("Wrong format")
                continue
            a , b = line
            if len(a) != 3:
                print("Wrong format")
                continue
            if a[0] != a[2]:
                print("Wrong format")
                continue
            if a[0] not in alph or a[1] not in alph:
                print("Wrong format")
                continue
            c = 0
            for i in range(len(b)-2):
                if a == b[i:i+3]:
                    c += 1
            print(c)
        except EOFError:break

if __name__ == "__main__":
    main()
