LIMIT_NUMBER = 100


def main():
    for i in range(1, LIMIT_NUMBER + 1):
        if (i % 3 == 0) and (i % 4 == 0):
            print('FizzBuzz', end=' ')
        elif i % 3 == 0:
            print('Fizz', end=' ')
        elif i % 5 == 0:
            print('Buzz', end=' ')
        else:
            print(i, end=' ')


if __name__ == '__main__':
    main()
