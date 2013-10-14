import logging
from unittest import TestCase
from logr import Logr
from qcond.helpers import sorted_append


class TestHelpers(TestCase):
    def setUp(self):
        Logr.configure(logging.DEBUG)

    def test_sorted_append(self):
        seq = [6, 5]
        sorted_append(seq, 9, lambda item: item < 9)
        self.assertSequenceEqual(seq, [9, 6, 5])

        seq = [6, 5]
        sorted_append(seq, 4, lambda item: item < 4)
        self.assertSequenceEqual(seq, [6, 5, 4])
