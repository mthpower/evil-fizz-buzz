import unittest

from fizzbuzz.sequence_generator import sequence_generator


class TestEvilFizzBuzz(unittest.TestCase):
    def test_generating_a_sequence(self):
        self.assertEqual(range(1, 101), sequence_generator(1, 100))
    