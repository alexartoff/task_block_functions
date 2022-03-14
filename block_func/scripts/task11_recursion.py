#!/usr/bin/env python


def is_odd(numb):
    if is_even(numb):
        return False
    return True


def is_even(numb):
    if numb % 2 == 1:
        return False
    return True


def is_odd_t(number):
    return False if number == 0 else is_even_t(number - 1)


def is_even_t(number):
    return True if number == 0 else is_odd_t(number - 1)


def main():
    print(is_odd(42), is_odd(99))
    print(is_even(42), is_even(99))


if __name__ == "__main__":
    main()
