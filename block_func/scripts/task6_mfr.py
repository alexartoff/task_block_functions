#!/usr/bin/env python


from functools import reduce
from operator import add, truth, getitem


def walk_t(dictionary, path):
    return reduce(getitem, path, dictionary)


def walk(dct, itr):
    iter_list = list(iter(itr))
    # out = getitem(dct, 'a')
    # outt = getitem(out, 7)
    # outtt = getitem(outt, 'b')
    dict_tmp = dct
    for i in iter_list:
        lst = getitem(dict_tmp, i)
        dict_tmp = lst
    return dict_tmp


def keep_truthful_t(items):
    return filter(truth, items)


def keep_truthful(itr):
    # filter()
    return filter(truth, iter(itr))


def abs_sum_t(numbers):
    return sum(map(abs, numbers))


def abs_sum(itr):
    # reduce()
    i = list(map(abs, iter(itr)))
    out = reduce(add, i, 0)
    return out


def main():
    print(list(keep_truthful([True, False, "", "foo"])))
    print(walk({'a': {7: {'b': 42}}}, ["a", 7, "b"]))
    print(abs_sum([-3, 7]))


if __name__ == "__main__":
    main()
