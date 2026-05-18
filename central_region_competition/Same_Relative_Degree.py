from collections import deque

def bfs(n , start , count , lines):
    if count == 0:
        return [start]
    q = deque([])
    q.append([start , 0])
    ans = []
    check = set()
    check.add(start)
    while q:
        position , c = q.popleft()

        for _next in lines[position]:
            if _next in check:continue
            check.add(_next)
            if c + 1 == count:
                ans.append(_next)
                continue
            q.append([_next , c + 1])

    return sorted(ans)

def main():
    while True:
        try:
            n , start , count = map(int , input().split())
            lines = {}
            for i in range(1 , n):
                a , b = map(int , input().split())
                if a not in lines:
                    lines[a] = set()
                if b not in lines:
                    lines[b] = set()
                lines[a].add(b)
                lines[b].add(a)
            ans = bfs(n , start , count , lines)
            print(' '.join(map(str , ans)))
        except EOFError:break

if __name__ == "__main__":
    main()
