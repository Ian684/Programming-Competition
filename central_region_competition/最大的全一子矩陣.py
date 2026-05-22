def get_all(line):

    arr = []

    for mask in range(1 , 1 << len(line)):
        subset = []
        for i in range(len(line)):
            if mask & (1 << i):
                subset.append(line[i])

        arr.append(tuple(subset))

    return arr

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        lines = {}
        for i in range(n):
            line = input().split()
            lines[i] = []
            for l in line:
                if l == '/':break
                j = int(l)
                lines[i].append(j-1)
        count = {}
        ans = -1
        for i in range(n):
            arr = get_all(lines[i])
            for s in arr:
                if s not in count:
                    count[s] = 0
                count[s] += 1
                ans = max(ans , count[s]*len(s))
        print(ans)

if __name__ == "__main__":
    main()
