def solve(line):

    def cal(l):
        a , b , op = l.split(',')
        a , b = int(a) , int(b)
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            return a // b

    ls = []
    i = 0
    while True:
        if '(' not in line and ')' not in line:break
        if line[i] == '(':
            ls.append(i)
            i += 1
            continue
        if line[i] == ')':
            r = i
            l = ls.pop()
            result = cal(line[l+1:r])
            i = l
            line = line[:l] + str(result) + line[r+1:]
            continue
        i += 1
    return int(line)

def main():
    t = int(input())
    for i in range(t):
        line = input()
        if '.' in line or '0' in line:
            print('Invalid Input!')
            continue
        print(solve(line))

if __name__ == "__main__":
    main()
