class StringSearchIndex:
    @staticmethod
    def brute_force_search_index(text: str, pattern: str) -> int:
        """Searches for a substring within a string using the brute-force method.

        Args:
        - text (str): The main string in which to search.
        - pattern (str): The substring to search for.

        Returns:
        - int: The starting index of the first occurrence of the pattern in the text.
            If the pattern is not found, the function returns -1.
        """
        for i, _ in enumerate(text):
            if i + len(pattern) > len(text):
                break

            is_match = True

            for j, character in enumerate(pattern):
                if text[i + j] != character:
                    is_match = False
                    break

            if is_match:
                return i

        return -1

    @staticmethod
    def boyer_moore_search(text: str, pattern: str) -> int:
        """Searches for a substring within a string using the Boyer-Moore method.

        Args:
        - text (str): The main string in which to search.
        - pattern (str): The substring to search for.

        Returns:
        - int: The starting index of the first occurrence of the pattern in the text.
            If the pattern is not found, the function returns -1.
        """
        skip_table: dict[str, int] = {
            char: len(pattern) - index - 1 for index, char in enumerate(pattern[:-1])
        }

        i = len(pattern) - 1
        while i < len(text):
            if i + len(pattern) > len(text):
                return -1

            is_match = True
            for j in range(len(pattern)):
                if text[i - j] != pattern[len(pattern) - 1 - j]:
                    is_match = False
                    break

            if is_match:
                return i - len(pattern) + 1

            # Move based on the skip table or skip the entire pattern's length
            i += skip_table.get(text[i], len(pattern))

        return -1


if __name__ == "__main__":
    # Sample usage
    result = StringSearchIndex.boyer_moore_search(
        "Success is not final, failure is not fatal.", "fail"
    )
    print(result)
