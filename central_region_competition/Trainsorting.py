###
def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        weights = []
        for j in range(n):
            weights.append(int(input()))
        lis = [1]*n
        lds = [1]*n
        ans = 0
        for i in range(n-1 , -1 , -1):
            for j in range(i+1 , n):
                if weights[i] < weights[j]:
                    lis[i] = max(lis[i] , lis[j]+1)
                if weights[i] > weights[j]:
                    lds[i] = max(lds[i] , lds[j]+1)
            ans = max(ans , lis[i]+lds[i]-1)
        print(ans)

if __name__ == "__main__":
    main()
