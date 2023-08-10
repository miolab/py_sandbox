class StringSearchIndex:
    TEXT = "Success is not final, failure is not fatal."
    PATTERN = "fail"

    def __init__(self):
        self.main()

    def main(self):
        print(self.brute_force_search_index(self.TEXT, self.PATTERN))

    def brute_force_search_index(self, text: str, pattern: str) -> int:
        # return dummy index
        return 1


if __name__ == "__main__":
    StringSearchIndex()
