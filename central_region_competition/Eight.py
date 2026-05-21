from collections import deque
import sys

def bfs():
    goal = "12345678x"
    q = deque([(goal, 8, "")])
    total = {goal: ""}
    moves = (
        (-3, 'd'),
        (3, 'u'),
        (1, 'l'),
        (-1, 'r')
    )
    while q:
        curr_state, x_idx, ans = q.popleft()
        
        r, c = x_idx // 3, x_idx % 3
        
        for idx_diff, d in moves:
            nr, nc = r, c
            if idx_diff == -3: nr -= 1
            elif idx_diff == 3: nr += 1
            elif idx_diff == 1: nc += 1
            elif idx_diff == -1: nc -= 1
            
            if 0 <= nr < 3 and 0 <= nc < 3:
                nxt_idx = x_idx + idx_diff
                
                state_list = list(curr_state)
                state_list[x_idx], state_list[nxt_idx] = state_list[nxt_idx], state_list[x_idx]
                nxt_state = "".join(state_list)
                
                if nxt_state not in total:
                    total[nxt_state] = ans + d
                    q.append((nxt_state, nxt_idx, ans + d))
    return total

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    total = bfs()
    t = int(input_data[0])
    idx = 1
    for _ in range(t):
        if idx >= len(input_data):
            break
        line = "".join(input_data[idx : idx + 9])
        idx += 9
        if line not in total:
            print("unsolvable") [cite: 35]
        else:
            print(total[line][::-1])
if __name__ == "__main__":
    main()
