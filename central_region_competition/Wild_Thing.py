def solve(aim , line):
    if not aim:
        if not line:
            return True
        return False
    if aim[0] == '*':
        for i in range(len(line)+1):
            if solve(aim[1:] , line[i:]):
                return True
        return False
    else:
        if not line:
            return False
        if aim[0] != line[0]:
            return False
        return solve(aim[1:] , line[1:])

def main():
    while True:
        ans = []
        try:
            aim = input()
            while True:
                line = input()
                if line == "":break
                if solve(aim , line):
                    ans.append(line)
        except EOFError:break
        if len(ans) != 0:
            print(f"MATCHES FOR THE PATTERN: {aim}")
            for a in ans:
                print(a)
            print()

if __name__ == "__main__":
    main()
