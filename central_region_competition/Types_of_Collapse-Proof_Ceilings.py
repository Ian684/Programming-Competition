def main():
    n , k = map(int , input().split())
    result = set()
    for i in range(n):
        arr = list(map(int , input().split()))
        tree = set()
        tree.add(0)
        value = {}
        value[0] = arr[0]
        for j in range(1 , k):
            p = arr[j]
            root = 0
            while True:
                if root not in tree:
                    value[root] = p
                    tree.add(root)
                    break
                if p < value[root]:
                    root = 2*root + 1
                elif p > value[root]:
                    root = 2*root + 2
        result.add(tuple(sorted(tree)))
    print(len(result))

if __name__ == "__main__":
    main()
