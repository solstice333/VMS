from pm import *
from inputparser import *


INPUT_PATH = "resources/"
OUTPUT_FILE = INPUT_PATH + '76027548.txt'


def main(pm):
    pm = PM(INPUT_PATH + "pm.txt")


def split_virtual_address(decimal_value):
    binary_number = "{0:028b}".format(decimal_value)
    s_bin = binary_number[:9]
    p_bin = binary_number[9:19]
    w_bin = binary_number[19:]
    return bin_to_dec(s_bin), bin_to_dec(p_bin), bin_to_dec(w_bin)


def bin_to_dec(binary_number):
    return int(binary_number, 2)


def get_entry(pm, addr):
    return pm[addr]


def eval_addr_for_rd(outfile, num):
    if num == -1:
        outfile.write('pf ')
    elif num == 0:
        outfile.write('err ')
    else:
        return True
    return False


def eval_addr_for_wr(outfile, pm, num, one_or_two_bits):
    if num == -1:
        outfile.write('pf ')
        return False
    elif num == 0:
        if one_or_two_bits == 1:
            pm.set_next_empty_bit()
        else:
            pm.set_next_empty_pair_bits()
    return True


if __name__ == '__main__':
    outfile = open(OUTPUT_FILE, 'w')

    pm = PM(INPUT_PATH + "pm.txt")
    virtual_addresses = Parser(INPUT_PATH + 'input2.txt')
    for wr, va in virtual_addresses.get_pairs():
        s, p, w = split_virtual_address(va)
        if wr == 1: # Write only
            seg_entry = pm[s]
            if eval_addr_for_wr(outfile, pm, seg_entry, 1):
                pt_entry = pm[pm[s]+p]
                if eval_addr_for_wr(outfile, pm, pt_entry, 2):
                    outfile.write(str(pm[pm[s]+p]+w) + ' ')
                else:
                    continue
            else:
                continue
        else: # Ready only
            if eval_addr_for_rd(outfile, pm[s]):
                if eval_addr_for_rd(outfile, pm[pm[s]+p]):
                    outfile.write(str(pm[pm[s]+p]+w) + ' ')
                else:
                    continue
            else:
                continue

    outfile.close()