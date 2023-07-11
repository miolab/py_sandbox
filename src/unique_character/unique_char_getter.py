class UniqueCharGetter:
    """A class used to get the first non-repeating character in a string."""

    @staticmethod
    def get_first_unique_char(characters: str) -> str | None:
        """Get the first non-repeating character in a string.
        If no unique character exists, return None.

        Parameters:
        characters (str): The input string

        Returns:
        str: The first non-repeating character in the string. If all characters are repeating, returns an empty string.
        """
        frequency: dict[str, int] = {}

        for char in characters:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

        for char in characters:
            if frequency[char] == 1:
                return char

        return None
