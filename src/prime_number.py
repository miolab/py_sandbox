import math

LIMIT_NUMBER = 1000


def main():
    for i in range(LIMIT_NUMBER):
        if is_prime(i):
            print(i, end=' ')


def is_prime(n: int) -> bool:
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


if __name__ == '__main__':
    main()
