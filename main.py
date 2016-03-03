from frame import *
from kyleParser import Parser

if __name__ == '__main__':
    m = [Frame(10) for i in range(10)]
    p = Parser("pm.txt")

    for s, f in p.get_pairs():
        print(s, f)
        m[0][s] = f
    print(m)
