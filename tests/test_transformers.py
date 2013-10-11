from unittest import TestCase
from qcond import MergeTransformer, SliceTransformer
from qcond.transformers.base import Transformer


class TestTransformer(TestCase):
    def test_run(self):
        transformer = Transformer()
        self.assertRaises(NotImplementedError, transformer.run, [])


class TestMergeTransformer(TestCase):
    def setUp(self):
        self.merge = MergeTransformer()

    def test_run(self):
        self.assertSequenceEqual(self.merge.run([
            "Don't Trust the B---- in Apartment 23",
            "Apartment 23",
            "Apt 23",
            "Don't Trust the B in Apt 23",
            "Don't Trust the B- in Apt 23",
            "Don't Trust the Bitch in Apartment 23",
            "Don't Trust the Bitch in Apt 23",
            "Dont Trust the Bitch in Apartment 23"
        ]), [
            'dont trust the',
            'dont trust the apt 23',
            'dont trust the apartment 23',
            'apt 23',
            'apartment 23'
        ])

    def test_merge(self):
        pass


class TestSliceTransformer(TestCase):
    def setUp(self):
        self.slice = SliceTransformer()

    def test_run(self):
        self.assertSequenceEqual(self.slice.run([
            "Don't Trust the B---- in Apartment 23",
            "Apartment 23",
            "Apt 23",
            "Don't Trust the B in Apt 23",
            "Don't Trust the B- in Apt 23",
            "Don't Trust the Bitch in Apartment 23",
            "Don't Trust the Bitch in Apt 23",
            "Dont Trust the Bitch in Apartment 23"
        ]), [
            'Apartment 23',
            'Apt 23',
            "Don't Trust the B in Apt 23",
            'Dont Trust the Bitch in Apartment 23'
        ])
