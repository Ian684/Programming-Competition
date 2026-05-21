def main():
    n = int(input())
    trees = list(map(int , input().split()))
    trees = sorted(trees , reverse=True)
    ans1 = -1
    for i in range(1 , n+1):
        ans1 = max(ans1 , i+trees[i-1])
    trees = trees[::-1]
    ans2 = -1
    for i in range(1 , n+1):
        ans2 = max(ans2 , i+trees[i-1])
    print(ans1 , ans2)

if __name__ == "__main__":
    main()
