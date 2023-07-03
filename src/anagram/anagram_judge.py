class AnagramJudgement:
    """A class used to check if two strings are anagrams.
    """

    @staticmethod
    def is_anagram(str_1: str, str_2: str) -> bool:
        """Judges if two strings are anagrams.

        Parameters:
        str_1 (str): The first string
        str_2 (str): The second string

        Returns:
        bool: True if the strings are anagrams, False otherwise
        """
        return sorted(str_1) == sorted(str_2)
