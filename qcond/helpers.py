from difflib import SequenceMatcher
import re


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


def similarity(a, b, swap_longest = True, case_sensitive = False):
    create_matcher(a, b, swap_longest, case_sensitive).quick_ratio()
