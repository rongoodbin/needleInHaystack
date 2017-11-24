import unittest
from needlehaystack import NeedleInHaystack

class TestNeedleInHaystack(unittest.TestCase):

    def setUp(self):
        pass
    def test_simplecases(self):
        needle = "abc"
        haystack = "abcdef"
        needleInHay = NeedleInHaystack(needle, haystack)
        self.assertEqual(needleInHay.findOccurrences(),['abc'])

        haystack = "abcdefcab"
        needleInHay = NeedleInHaystack(needle, haystack)
        self.assertEqual(needleInHay.findOccurrences(),['abc','cab'])

    def test_nonefound(self):
        needle = "xyz"
        haystack = "abcdef"
        needleInHay = NeedleInHaystack(needle, haystack)
        self.assertEqual(needleInHay.findOccurrences(),[])
       
if __name__ == '__main__':
    unittest.main()
