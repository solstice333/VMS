import unittest
from cpu import CPU
import os


INPUT_PATH = "../resources/"
OUTPUT_FILE = INPUT_PATH + '76027548.txt'
INITFILE = INPUT_PATH + "pm.txt"
VAFILE = INPUT_PATH + "input2.txt"


class TestCPU(unittest.TestCase):
    def setUp(self):
        self.cpu = CPU(OUTPUT_FILE, INITFILE, VAFILE)

    def test_convert_va_to_pa(self):
        self.cpu.convert_va_to_pa(False)

    def test_write(self):
        self.cpu._write(0, 0, 0)
        self.assertEqual(str(self.cpu._pm._bitmap), "0x7f")
        self.assertEqual(self.cpu._pm[0], 1024)
        self.assertEqual(self.cpu._pm[2], 2048)
        self.assertEqual(self.cpu._pm[2048], 512)
        self.assertEqual(self.cpu._pm[2049], -1)
        self.assertEqual(self.cpu._pm[1024], 3072)

if __name__ == "__main__":
    unittest.main()