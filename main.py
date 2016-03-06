from cpu import *


INPUT_PATH = "resources/"
OUTPUT_FILE = INPUT_PATH + '76027548.txt'
INITFILE = INPUT_PATH + "pm.txt"
VAFILE = INPUT_PATH + "input2.txt"


def main():
    cpu = CPU(OUTPUT_FILE, INITFILE, VAFILE)
    cpu.convert_va_to_pa(True)


if __name__ == '__main__':
    main()
