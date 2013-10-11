from qcond.transformers.base import Transformer


COMMON_WORDS = [
    'the'
]


class StripCommonTransformer(Transformer):
    def run(self, titles):
        return [title for title in titles if title.lower() not in COMMON_WORDS]
