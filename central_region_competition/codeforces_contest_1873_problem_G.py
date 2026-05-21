import sys

def solve(s):
    total_a = s.count('A')
    if total_a == 0 or 'B' not in s:
        return 0
    if s[0] == 'B' or s[-1] == 'B' or 'BB' in s:
        return total_a
    min_block = 10**18
    cur = 0
    for ch in s:
        if ch == 'A':
            cur += 1
        else:
            min_block = min(min_block, cur)
            cur = 0
    min_block = min(min_block, cur)
    return total_a - min_block
def main():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    ans = []

    for i in range(1, t + 1):
        ans.append(str(solve(data[i])))
    print('\n'.join(ans))
if __name__ == "__main__":
    main()
