import pytest
from anagram_judge import AnagramJudgement


def test_is_anagram():
    assert AnagramJudgement.is_anagram('listen', 'silent') == True
    assert AnagramJudgement.is_anagram('abcde', 'fghij') == False
    assert AnagramJudgement.is_anagram('aaa', 'aaa') == True


def test_is_anagram_type_error():
    with pytest.raises(TypeError):
        AnagramJudgement.is_anagram(123, 321)

    with pytest.raises(TypeError):
        AnagramJudgement.is_anagram('abc', 321)

    with pytest.raises(TypeError):
        AnagramJudgement.is_anagram(321, 'abc')

    with pytest.raises(TypeError):
        AnagramJudgement.is_anagram(['a', 'b', 'c'], ['c', 'b', 'a'])
