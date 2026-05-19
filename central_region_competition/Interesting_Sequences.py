def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [-1]+list(map(int , input().split()))
        dp = [0]*(n+1)
        last_pos = {}
        for i in range(1 , n+1):
            if arr[i] in last_pos:
                dp[i] = max(dp[i-1] , dp[last_pos[arr[i]]]+1)
            else:
                dp[i] = dp[i-1]
            last_pos[arr[i]] = i
        print(dp[-1])

if __name__ == "__main__":
    main()
