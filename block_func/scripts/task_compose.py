#!/usr/bin/env python


def compose(func_one, func_two):
    def inner(x):
        return func_one(func_two(x))
    return inner


def compose_t(f, g):
    return lambda x: f(g(x))


def add5(x):
    return x + 5


def mul3(x):
    return x * 3


def main():
    print(compose(mul3, add5)(1))


if __name__ == "__main__":
    main()
