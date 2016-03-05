from frame import Frame
import unittest


class TestFrame(unittest.TestCase):
    def setUp(self):
        self.f = Frame()

    def test_set(self):
        self.f[0] = 2
        self.assertTrue(self.f[0], 2)
        self.f[511] = 3
        self.assertTrue(self.f[511], 3)
        self.assertRaises(IndexError, self.f.__getitem__, 512)
        self.assertRaises(IndexError, self.f.__getitem__, -1)
        self.assertRaises(IndexError, self.f.__setitem__, 512, 0)
        self.assertRaises(IndexError, self.f.__setitem__, -1, 0)