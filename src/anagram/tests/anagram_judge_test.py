import pytest
from anagram_judge import AnagramJudgement


def test_is_anagram():
    assert AnagramJudgement.is_anagram('listen', 'silent') == True
    assert AnagramJudgement.is_anagram('abcde', 'fghij') == False
    assert AnagramJudgement.is_anagram('aaa', 'aaa') == True
