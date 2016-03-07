from pm import *
from tlb import *
from exceptions import *


class CPU:
    def __init__(self, outfile, initfile, vafile):
        self._outfile = open(outfile, "w")
        self._pm = PM(initfile)
        self._pairs_of_virtual_addresses = Parser(vafile)
        self._tlb = TLB(self._pm, self._outfile)

    def convert_va_to_pa(self, tlb):
        if tlb:
            for wr, va in self._pairs_of_virtual_addresses.get_pairs():
                sp, w = self._split_virtual_address_to_strs(va)
                index = self._tlb.find_matching_buffer(sp)

                if index == -1:  # reusing code from else...
                    self._read_write(wr, va)
                    self._tlb.replace_old_buffer(sp)
                else:
                    self._tlb.update_matching_buffer(index)
                    page_entry = self._tlb.get_f(index) + int(w, 2)
                    self._outfile.write(str(page_entry) + " ")
        else:
            for wr, va in self._pairs_of_virtual_addresses.get_pairs():
                self._read_write(wr, va)

    def _read_write(self, wr, va):
        s, p, w = self._split_virtual_address_to_ints(va)

        if wr == 1:  # Write only
            self._write(s, p, w)
        else:  # Ready only
            self._read(s, p, w)

    def _write(self, s, p, w):
        self._safe_alloc(s, p)
        self._read(s, p, w)

    def _read(self, s, p, w):
        entry = 0
        try:
            self._eval(s) and self._eval(self._pm[s] + p)
        except ZeroError:
            self._outfile.write('err ')
        except PFError:
            self._outfile.write('pf ')
        else:
            entry = self._pm[self._pm[s] + p] + w
            self._outfile.write("{0} ".format(entry))

    def _split_virtual_address_to_ints(self, decimal_value):
        bin_to_dec = lambda bin_num: int(bin_num, 2)
        binary_number = "{0:028b}".format(decimal_value)
        s_bin = binary_number[:9]
        p_bin = binary_number[9:19]
        w_bin = binary_number[19:]
        return bin_to_dec(s_bin), bin_to_dec(p_bin), bin_to_dec(w_bin)

    def _split_virtual_address_to_strs(self, decimal_value):
        binary_number = "{0:028b}".format(decimal_value)
        sp_bin = binary_number[:19]
        w_bin = binary_number[19:]
        return sp_bin, w_bin

    def _eval(self, idx):
        addr = self._pm[idx]
        if addr == 0:
            raise ZeroError
        elif addr < 0:
            raise PFError
        else:
            return addr

    def _safe_alloc(self, s, p):
        try:
            self._eval(s)
        except ZeroError:
            self._alloc(s, True)
            self._alloc(self._pm[s] + p, False)
        except PFError:
            pass

        try:
            self._eval(self._pm[s] + p)
        except ZeroError:
            self._alloc(self._pm[s] + p, False)
        except PFError:
            pass

    def _alloc(self, idx, is_page_table):
        addr = self._pm[idx]
        if addr == 0:
            if is_page_table:
                self._pm.fralloc(idx, 2)
            else:
                self._pm.fralloc(idx, 1)
        return addr

    def flush(self):
        self._outfile.flush()

    def __del__(self):
        self._outfile.close()