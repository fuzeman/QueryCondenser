from difflib import SequenceMatcher
import re
import sys


PY3 = sys.version_info[0] == 3


def simplify(s):
    s = s.lower()
    s = re.sub(r"(\w)'(\w)", r"\1\2", s)
    return s


def strip(s):
    return re.sub(r"^(\W*)(.*?)(\W*)$", r"\2", s)


def create_matcher(a, b, swap_longest = True, case_sensitive = False):
    # Ensure longest string is a
    if swap_longest and len(b) > len(a):
        a_ = a
        a = b
        b = a_

    if not case_sensitive:
        a = a.upper()
        b = b.upper()

    return SequenceMatcher(None, a, b)


def first(function_or_none, sequence):
    if PY3:
        for item in filter(function_or_none, sequence):
            return item
    else:
        result = filter(function_or_none, sequence)
        if len(result):
            return result[0]

    return None
