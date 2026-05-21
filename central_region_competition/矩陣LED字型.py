def cal_all_value(aim , line , check):
    total = []
    for i in range(len(aim)):
        temp = check[aim[i]][::]
        if line[i] == 'A':
            for j in range(5):
                temp[j] = bin(temp[j])[2:].zfill(7)
            total.append(temp)
        elif line[i] == 'B':
            t = []
            for j in range(5):
                t.append((bin(temp[j])[2:].zfill(7))[::-1])
            total.append(t)
        else:
            for j in range(5):
                temp[j] = bin(127^temp[j])[2:].zfill(7)
            if line[i] == 'C':
                total.append(temp)
            else:
                t = []
                for j in range(5):
                    t.append(temp[j][::-1])
                total.append(t)
    return total

def input_bit(stages, bit):
    next_st = [0] * 16
    xor_top = bit ^ stages[0]
    next_st[15] = xor_top
    next_st[14] = stages[15]
    next_st[13] = stages[14] ^ xor_top
    for i in range(1, 13):
        next_st[i] = stages[i+1]
    next_st[0] = stages[1] ^ xor_top
    return next_st

def cal_stage_result(stages):
    value = 0
    for i in range(16):
        value += stages[i] << (i)
    return value

def main():
    m = int(input())
    check = {}
    for _ in range(m):
        line = input().split(',')
        for l in range(len(line)):
            line[l] = line[l].strip()
        check[line[0]] = list(map(int , line[1:]))
    aim = input()
    line = input()
    total = cal_all_value(aim , line , check)
    stages = [0]*16
    for i in range(6 , -1 , -1):
        temp = []
        for j in range(len(total)):
            for k in range(5):
                bit = int(total[j][k][i])
                stages = input_bit(stages , bit)
        print(cal_stage_result(stages))

if __name__ == "__main__":
    main()
