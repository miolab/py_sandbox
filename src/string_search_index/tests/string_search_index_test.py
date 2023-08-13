import pytest
from string_search_index import StringSearchIndex


def test_brute_force_search_index__normal_case():
    """Normal case tests."""
    assert StringSearchIndex.brute_force_search_index("abcdef", "bc") == 1
