def fibonacci(num):
    match num:
        case 0:
            return 1
        case 1:
            return 1
        case _:
            return fibonacci(num - 1) + fibonacci(num - 2)


for i in range(10):
    print(fibonacci(i))
