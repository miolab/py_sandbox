import pytest
from string_search_index import StringSearchIndex


def test_brute_force_search_index__normal_case():
    # Normal case tests.
    assert StringSearchIndex.brute_force_search_index("abcdefg", "bc") == 1
    assert StringSearchIndex.brute_force_search_index("Hello world", "wor") == 6

    # Target substring does NOT exist case tests.
    assert StringSearchIndex.brute_force_search_index("abc", "xyz") == -1
    assert StringSearchIndex.brute_force_search_index("abc", "abcde") == -1


def test_boyer_moore_search_index__normal_case():
    # Normal case tests.
    assert StringSearchIndex.boyer_moore_search_index("abcdefg", "bc") == 1
    assert StringSearchIndex.boyer_moore_search_index("Hello world", "wor") == 6

    # Target substring does NOT exist case tests.
    assert StringSearchIndex.boyer_moore_search_index("abc", "xyz") == -1
    assert StringSearchIndex.boyer_moore_search_index("abc", "abcde") == -1
