def main():
    alph = {'A':17 , 'B':18 , 'C':16 , 'W':21 , 'X':18}
    while True:
        try:
            n = int(input())
            line = input().split()
            if n == 0 and len(line) == 1 and line[0] == "YZYZ":break
            letter = 0
            word = -1
            for i in range(len(line)):
                word += 1
                letter += len(line[i]) - 1
                for j in range(len(line[i])):
                    n -= alph[line[i][j]]
            if n <= 3*letter + 10*word:
                letters = [3]*letter
                words = [10]*word
            else:
                if word == 0 and letter == 0:
                    letters = []
                    words = []
                elif letter == 0:
                    letters = []
                    second = n // word
                    words = [second]*word
                    if n - second * word > 0:
                        for i in range(n - second*word):
                            words[i] += 1
                elif word == 0:
                    words = []
                    first = n // letter
                    letters = [first]*letter
                else:
                    total = letter + 3*word
                    first = n // total
                    letters = [first]*letter
                    n -= first*letter
                    second = n // word
                    words = [second]*word
                    n -= second*word
                    if n > 0:
                        for i in range(n):
                            words[i] += 1
            k = 0
            for i in range(len(line)):
                for j in range(len(line[i])):
                    print(line[i][j] , end="")
                    if j != len(line[i]) - 1:
                        print(f"({letters[k]})" , end="")
                        k += 1
                if i < len(words):
                    print(f"({words[i]})" , end="")    
            print()
        except EOFError:break

if __name__ == "__main__":
    main()
