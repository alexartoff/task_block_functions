#!/usr/bin/env python


from math import sqrt


def filter_map(func, itr):
    out = list()
    for i in itr:
        if func(i)[0]:
            out.append(func(i)[1])
    return out


def main():
    print(filter_map(sqrt, [4, -5, -2, 9]))


if __name__ == "__main__":
    main()
