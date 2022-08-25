import math

LIMIT_NUMBER = 10000


def main():
    number = input_number()

    if number < 1:
        print('正の整数ではありません')
        return
    if number > LIMIT_NUMBER:
        print(f'{LIMIT_NUMBER}以下の数を入力してください')
        return

    for i in range(number):
        if is_prime(i):
            print(i, end=' ')


def is_prime(n: int) -> bool:
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def input_number() -> int:
    input_number = int(
        input(f'正の整数を入力: ')
    )

    return input_number


if __name__ == '__main__':
    main()
