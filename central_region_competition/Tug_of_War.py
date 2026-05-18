def main():
    c = int(input())
    while c != 0:
        line = input()
        if line == "":continue
        n = int(line)
        arr = []
        for i in range(n):
            arr.append(int(input()))
        total = sum(arr)
        target = total // 2
        k = n // 2
        dp = [[False]*(target+1) for _ in range(k+1)]
        dp[0][0] = True
        for w in arr:
            for i in range(k , 0 , -1):
                for j in range(target , w-1 , -1):
                    if dp[i-1][j-w]:
                        dp[i][j] = True
        for i in range(target , -1 , -1):
            if dp[k][i]:
                a = i
                b = total - i
                break
        print(min(a , b) , max(a , b))
        if c != 1:
            print()
        c -= 1

if __name__ == "__main__":
    main()
