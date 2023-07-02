class FizzBuzz:
    LIMIT_NUMBER: int = 100


    def main(self) -> None:
        for i in range(1, self.LIMIT_NUMBER + 1):
            if (i % 3 == 0) and (i % 4 == 0):
                print('FizzBuzz', end=' ')
            elif i % 3 == 0:
                print('Fizz', end=' ')
            elif i % 5 == 0:
                print('Buzz', end=' ')
            else:
                print(i, end=' ')


if __name__ == '__main__':
    FizzBuzz().main()
