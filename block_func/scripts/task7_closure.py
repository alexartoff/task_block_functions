#!/usr/bin/env python


from operator import add


def partial_apply(fnc, param):
    def inner(param_next):
        out = fnc(param, param_next)
        return out
    return inner


def flip(fnc):
    def inner(one, two):
        return fnc(two, one)
    return inner


def greet(name, surname):
    return f'Hello, {name} {surname}!'


def main():
    f = partial_apply(greet, 'Dorian')
    print(f('Grey'))
    print(list(map(partial_apply(add, 10), [1, 2, 3])))
    ff = flip(greet)
    print(ff('Alex', 'Tarrr'))


if __name__ == "__main__":
    main()
