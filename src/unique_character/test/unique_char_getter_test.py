import pytest
from unique_char_getter import UniqueCharGetter


def test_get_first_unique_char():
    assert UniqueCharGetter.get_first_unique_char("alphabet") == "l"
    assert UniqueCharGetter.get_first_unique_char("cat") == "c"
    assert UniqueCharGetter.get_first_unique_char("aabbcc") is None
