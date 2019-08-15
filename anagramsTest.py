import anagrams
import unittest


class testAnagrams(unittest.TestCase):

    def test_case_is_insensitive(self):
        onlyAs = anagrams.anagramDict(['a', 'A'])
        self.assertEqual(onlyAs.getAnagram('A'), ['a', 'A'])
        self.assertEqual(onlyAs.getAnagram('a'), ['a', 'A'])

    def test_order_does_not_matter(self):
        post = anagrams.anagramDict(['post', 'pots', 'spot', 'tops', 'stop'])
        self.assertEqual(post.getAnagram('opts'),
                         ['post', 'pots', 'spot', 'tops', 'stop'])

    def test_noise_is_not_returned(self):
        sheep = anagrams.anagramDict(['baa', 'aba', 'baaaaa', 'aBA'])
        self.assertEqual(sheep.getAnagram('aab'), ['baa', 'aba', 'aBA'])


if __name__ == '__main__':
    unittest.main()
