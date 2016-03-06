from cpu import *


INPUT_PATH = "resources/"
OUTPUT_FILE = INPUT_PATH + '76027548.txt'


def main():
    outfile = open(OUTPUT_FILE, 'w')
    cpu = CPU(outfile)
    outfile.close()


if __name__ == '__main__':
    main()
