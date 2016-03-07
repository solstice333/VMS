import unittest
from cpu import CPU
import re

INPUT_PATH = "../resources/"
OUTPUT_FILE = INPUT_PATH + '76027548.txt'
INITFILE = INPUT_PATH + "pm.txt"
VAFILE = INPUT_PATH + "input2.txt"


class TestCPU(unittest.TestCase):
    def test_convert_va_to_pa(self):
        cpu = CPU(INPUT_PATH + "foo.txt", INITFILE, VAFILE)
        cpu.convert_va_to_pa(False)
        cpu.flush()

        with open(INPUT_PATH + "foo.txt") as file:
            elems = re.findall(r"(\w+)\s*", file.readline(), re.I)
            self.assertEqual(elems[0], "err")
            self.assertEqual(elems[1], "512")
            self.assertEqual(elems[2], "522")
            self.assertEqual(elems[3], "pf")

    def test_write(self):
        cpu = CPU(OUTPUT_FILE, INITFILE, VAFILE)
        cpu._write(0, 0, 0)
        self.assertEqual(str(cpu._pm._bitmap), "0x7f")
        self.assertEqual(cpu._pm[0], 1024)
        self.assertEqual(cpu._pm[2], 2048)
        self.assertEqual(cpu._pm[2048], 512)
        self.assertEqual(cpu._pm[2049], -1)
        self.assertEqual(cpu._pm[1024], 3072)

    def test_broken_stuff(self):
        cpu = CPU(INPUT_PATH + "foo.txt", INPUT_PATH + "initPMTestCases.txt",\
         INPUT_PATH + "initVATestCases.txt")
        cpu.convert_va_to_pa(False)
        cpu.flush()

        with open(INPUT_PATH + "foo.txt") as file:
            elems = re.findall(r"(\w+)\s*", file.readline(), re.I)
            self.assertEqual(elems[0], "1400")
            self.assertEqual(elems[1], "1400")
            self.assertEqual(elems[2], "1952")

if __name__ == "__main__":
    unittest.main()