#!/usr/bin/env python


def memoized(fnc):
    dct = {}

    def inner(x):
        # print('before')
        if not (x in dct.keys()):
            dct[x] = fnc(x)
        return dct[x]
        # print('after')
    return inner


@memoized
def f(x):
    print('Calculating...')
    return x * 10


counter = [0]


@memoized
def xor(byte):
    counter[0] += 1
    return 255 ^ byte


def main():
    f1 = f(10)
    f2 = f(10)
    f3 = f(20)
    f4 = f(10)
    print(f1,f2,f3,f4)
    # res = xor(xor(42))
    # print(res, counter)
    res2 = xor(42) + xor(xor(42))
    res3 = xor(127)
    res4 = xor(128)
    print(res2, res3, res4)
    print(counter)


if __name__ == "__main__":
    main()