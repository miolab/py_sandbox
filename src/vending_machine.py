COINS = (
    5000,
    1000,
    500,
    100,
    50,
    10,
    5,
    1
)


def main():
    product = input_product()
    price = input_price(product)

    change = price - product

    if (is_available_price(change) == False):
        return

    print(f'\nお釣り: {str(change)}円\n')

    for i in COINS:
        coin_numbers = change // i
        change %= i

        print(f'{str(i)}円: {str(coin_numbers)}枚')


def input_product() -> int:
    input_product = int(
        input('商品価格 (円): ')
    )

    return input_product


def input_price(product: int) -> int:
    input_price = int(
        input(f'投入する金額を入力 (商品価格{product}円): ')
    )

    return input_price


def is_available_price(change: int) -> bool:
    if change < 0:
        print('商品価格を下回っています')
        return False

    return True


if __name__ == '__main__':
    main()
