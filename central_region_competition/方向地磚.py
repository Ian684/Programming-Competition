from collections import *

def bfs(m , arr , start , end):
    q = deque([])
    direction = arr[start[0]][start[1]][1]
    q.append([start[0] , start[1] , direction])
    result = [1]

    while q:
        x , y , direction = q.popleft()
        if direction == 'E':
            dx , dy = 0 , 1
        elif direction == 'W':
            dx , dy = 0 , -1
        elif direction == 'N':
            dx , dy = -1 , 0
        elif direction == 'S':
            dx , dy = 1 , 0
        smallest = [1 << 60 , -1 , -1]
        for i in range(1 , m):
            nx , ny = x + i*dx , y + i*dy
            if nx < 0 or nx >= m or ny < 0 or ny >= m:break
            if arr[nx][ny][0] < smallest[0] and arr[nx][ny][0] > arr[x][y][0]:
                smallest = [arr[nx][ny][0] , nx , ny]
        if smallest[0] == 1 << 60:
            return result
        result.append(smallest[0])
        if smallest[0] == m**2:
            return result
        q.append([smallest[1] , smallest[2] , arr[smallest[1]][smallest[2]][1]])
    return None


def main():
    m = int(input())
    arr = []
    for i in range(m):
        line = input().split()
        arr.append([])
        for j in range(0 , 2*m , 2):
            if int(line[j]) == 1:
                start = [i , j//2]
            elif int(line[j]) == m**2:
                end = [i , j//2]
            arr[-1].append([int(line[j]) , line[j+1]])
    
    result = bfs(m , arr , start , end)
    if len(result) >= 3:
        print(result[-3] , result[-2] , result[-1])

if __name__ == "__main__":
    main()
