from bitmap import Bitmap
from bitmap import TooDamnMuchDammitError
import re
import unittest


class TestBitmap(unittest.TestCase):
   def test_ctor(self):
      b = Bitmap()
      self.assertTrue(b)
      bitset = b.get_bitmap_as_indices()
      self.assertTrue(not len(bitset))

   def test_overloaded_ctor(self):
      b = Bitmap(0x0FF0F0)
      self.assertTrue(b)
      bitset = b.get_bitmap_as_indices()
      self.assertTrue(len(bitset) == 12)

      i = 0
      for j in range(4, 8):
         self.assertEqual(bitset[i], j)
         i += 1

      for j in range(12, 20):
         self.assertEqual(bitset[i], j)
         i += 1

   def test_max_bits(self):
      b = Bitmap(2**1024 - 1)
      self.assertTrue(b)
      bitset = b.get_bitmap_as_indices()
      self.assertTrue(len(bitset) == 1024)

   def test_raise_toodamnmuchdammiterror(self):
      self.assertRaises(TooDamnMuchDammitError, Bitmap, 2**1024)

   def test_is_bit_set(self):
      b = Bitmap(0xAAAAAAAA55555555)
      bitset = b.get_bitmap_as_indices()

      for i in range(64):
         if (i < 32):
            if (i % 2):
               self.assertFalse(b.is_bit_set(i))
            else:
               self.assertTrue(b.is_bit_set(i))
         else:
            if (i % 2):
               self.assertTrue(b.is_bit_set(i))
            else:
               self.assertFalse(b.is_bit_set(i))

      self.assertRaises(TooDamnMuchDammitError, b.is_bit_set, 1024)

   def test_set_bit(self):
      b = Bitmap()

      b.set_bit(64)
      b.set_bit(0)
      b.set_bit(1023)

      self.assertTrue(b.is_bit_set(64))
      self.assertTrue(b.is_bit_set(0))
      self.assertTrue(b.is_bit_set(1023))

      for i in range(1024):
         if i != 64 and i != 0 and i != 1023:
            self.assertFalse(b.is_bit_set(i))

      self.assertRaises(TooDamnMuchDammitError, b.set_bit, 1024)

   def test_get_bitmask(self):
      b = Bitmap(0xAA55)
      self.assertEqual(str(b), "0xaa55")

   def test_clr_bit(self):
      b = Bitmap(0xAA55)
      b.clr_bit(0);
      self.assertEqual(str(b), "0xaa54")
      b.clr_bit(1);
      self.assertEqual(str(b), "0xaa54")
      b.clr_bit(2);
      self.assertEqual(str(b), "0xaa50")
      b.clr_bit(4);
      self.assertEqual(str(b), "0xaa40")
      b.clr_bit(6);
      self.assertEqual(str(b), "0xaa00")
      b.clr_bit(15)
      self.assertEqual(str(b), "0x2a00")
      b.set_bit(1023)
      self.assertTrue(b.is_bit_set(1023) and re.search(r"2a00$", str(b), re.I))
      b.clr_bit(1023)
      self.assertTrue(str(b), "0x2a00")
      self.assertRaises(TooDamnMuchDammitError, b.clr_bit, 1024)

if __name__ == "__main__":
   unittest.main() 
