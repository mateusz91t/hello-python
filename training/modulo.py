def print_modulo(base: int, max_exponent: int, modulus: int) -> None:
    exponent = 0
    while exponent <= max_exponent:
        print(f"{base}^{exponent} mod {modulus}=", base ** exponent % modulus)
        exponent += 1


# print_modulo(3, 17, 17)
# print_modulo(3, 50, 17)
print_modulo(4, 50, 19)
