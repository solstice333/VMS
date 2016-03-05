import unittest
from pm import PM


INPUT_PATH = "../resources/"


class TestPM(unittest.TestCase):
    def test_init(self):
        p = PM(str(INPUT_PATH) + "pm.txt")
        self.assertEqual(p.get_bitmap(), "0x33")

    def test_get_index_from_words(self):
        self.assertEqual(PM.get_index_from_words(700), 1)
        self.assertEqual(PM.get_index_from_words(511), 0)
        self.assertEqual(PM.get_index_from_words(1023), 1)
        self.assertEqual(PM.get_index_from_words(1024), 2)
        self.assertEqual(PM.get_index_from_words(1535), 2)


if __name__ == "__main__":
    unittest.main()