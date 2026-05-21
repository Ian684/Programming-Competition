def spfa(m , lines , start , end):






def main():
    while True:
        try:
            m = int(input())
            lines = {}
            d = set()
            _out = {}
            _in = {}
            for i in range(m):
                a , b = map(int , input().split())
                if (a , b) not in lines:
                    lines[(a , b)] = 0
                d.add(a)
                d.add(b)
                lines[(a , b)] += 1
                if a not in _in:
                    _in[a] = 0
                if a not in _out:
                    _out[a] = 0
                if b not in _in:
                    _in[b] = 0
                if b not in _out:
                    _out[b] = 0
                _out[a] += 1
                _in[b] += 1
            start = []
            end = []
            for k in d:
                if _out[k] - _in[k] > 0:
                    start.append(k)
                elif _out[k] - _in[k] < 0:
                    end.append(k)
            print(m - spfa(m , lines , start , end))

if __name__ == "__main__":
    main()
