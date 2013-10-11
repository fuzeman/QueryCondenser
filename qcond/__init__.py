from qcond.transformers.merge import MergeTransformer
from qcond.transformers.slice import SliceTransformer
from qcond.transformers.strip_common import StripCommonTransformer


class QueryCondenser(object):
    def __init__(self):
        self.transformers = [
            MergeTransformer(),
            SliceTransformer(),
            StripCommonTransformer()
        ]

    def distinct(self, titles):
        for transformer in self.transformers:
            titles = transformer.run(titles)

        return titles
