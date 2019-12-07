import unittest
import main


class TestAnagramFinder(unittest.TestCase):

    def test_anagram_exists(self):
        self.assertRegex(str(main.anagram_finder("act")), "cat")

    def test_anagram_not_exists(self):
        self.assertRegex(str(main.anagram_finder("xact")), "No anagrams found")


if __name__ == '__main__':
    unittest.main()
