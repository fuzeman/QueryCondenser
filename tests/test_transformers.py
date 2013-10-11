from unittest import TestCase
from qcond.transformers.base import Transformer


class TestTransformer(TestCase):
    def test_run(self):
        transformer = Transformer()
        self.assertRaises(NotImplementedError, transformer.run, [])


class TestMergeTransformer(TestCase):
    def test_run(self):
        self.fail()

    def test_merge(self):
        self.fail()


class TestSliceTransformer(TestCase):
    def test_run(self):
        self.fail()
