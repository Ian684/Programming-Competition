def main():
    with open("words.txt", "r", encoding="utf-8") as file:
        for line in file:
            s = line.strip()
            if not s:
                continue
            s = s.lower()
            ss = {}
            for i in s:
                if i not in ss:
                    ss[i] = 0
                ss[i] += 1
            c = set()
            valid = True
            for k , v in ss.items():
                if v in c:
                    valid = False
                    break
                c.add(v)
            if valid and len(c) >= 2:
                print("Yes")
            else:
                print("No")

if __name__ == "__main__":
    main()
