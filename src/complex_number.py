def add_float_and_complex(a: float, b: complex) -> complex:
    assert type(a) == float
    assert type(b) == complex

    return a + b


print(add_float_and_complex(
    1.1,
    2.1j
))
