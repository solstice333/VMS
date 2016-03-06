import unittest
from pm import PM


INPUT_PATH = "../resources/"


class TestPM(unittest.TestCase):
    def setUp(self):
        self.p = PM(INPUT_PATH + "pm.txt")

    def test_init(self):
        self.assertEqual(self.p.get_bitmap(), "0x33")

    def test_get_index_from_words(self):
        self.assertEqual(PM.get_index_from_words(700), 1)
        self.assertEqual(PM.get_index_from_words(511), 0)
        self.assertEqual(PM.get_index_from_words(1023), 1)
        self.assertEqual(PM.get_index_from_words(1024), 2)
        self.assertEqual(PM.get_index_from_words(1535), 2)

    def test_seg_table_init(self):
        self.assertEqual(self.p[2], 2048) # 2 2048

    def test_page_table_init(self):
        self.assertEqual(self.p[2048], 512) # 0 2 512
        self.assertEqual(self.p[2049], -1) # 1 2 -1

    def test_out_of_bounds(self):
        self.assertRaises(IndexError, self.p.__getitem__, 524288)
        self.assertEqual(self.p[524287], 0)
        self.assertRaises(IndexError, self.p.__getitem__, -1)
        self.assertEqual(self.p[0], 0)

    def test_get_set_by_idx(self):
        self.p[524287] = 100
        self.assertEqual(self.p[524287], 100)
        self.p[0] = 200
        self.assertEqual(self.p[0], 200)

    def test_get_words_from_index(self):
        self.assertEqual(PM.get_words_from_index(5), 2560)

    def test_fralloc(self):
        self.assertEqual(self.p[0], 0)
        self.p.fralloc(0, 2)
        self.assertEqual(str(self.p._bitmap), "0x3f")
        self.assertEqual(self.p[0], 1024)
        self.p.fralloc(1025, 1)
        self.assertEqual(str(self.p._bitmap), "0x7f")
        self.assertEqual(self.p[1025], 3072)


if __name__ == "__main__":
    unittest.main()