import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    t = int(next(iterator))
    
    for _ in range(t):
        n = int(next(iterator))
        arr = [int(next(iterator)) for _ in range(n)]
        last_pos = {}
        ans = 0
        last_match_idx = -1 
        for i in range(n):
            num = arr[i]
            if num in last_pos and last_pos[num] >= last_match_idx:
                ans += 1
                last_match_idx = i 
            last_pos[num] = i
        print(ans)
if __name__ == "__main__":
    main()
