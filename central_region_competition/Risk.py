from collections import deque

def bfs(lines , start , end):
    q = deque([])
    q.append([0 , start])
    check = [False]*21
    check[start] = True

    while q:
        count , position = q.popleft()
        
        for _next in lines[position]:
            if check[_next]:continue
            if _next == end:return count + 1
            check[_next] = True
            q.append([count + 1 , _next])

    return None

def main():
    while True:
        lines = {}
        for i in range(1 , 21):
            lines[i] = set()
        try:
            for i in range(1 , 20):
                line = list(map(int , input().split()))
                for l in line[1:]:
                    lines[i].add(l)
                    lines[l].add(i)
            n = int(input())
            for i in range(n):
                start , end = map(int , input().split())
                ans = bfs(lines , start , end)
                if ans is None:
                    print("yo")
                else:
                    print(start , end , ans)
        except EOFError:break

if __name__ == "__main__":
    main()
