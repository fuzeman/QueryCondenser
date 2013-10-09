from qcond.transformers.merge import MergeTransformer
from qcond.transformers.slice import SliceTransformer


class QueryCondenser(object):
    def __init__(self):
        self.merge = MergeTransformer()
        self.slice = SliceTransformer()

    def distinct(self, titles):
        titles = self.merge.run(titles)
        titles = self.slice.run(titles)

        return titles
