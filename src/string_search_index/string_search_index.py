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


if __name__ == "__main__":
    result = StringSearchIndex.brute_force_search_index(
        "Success is not final, failure is not fatal.", "fail"
    )
    print(result)
