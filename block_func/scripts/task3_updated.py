#!/usr/bin/env python


def updated_t(dictionary, **kwargs):
    new = dictionary.copy()
    new.update(kwargs)
    return new


def updated(dct, **kwargs):
    out_dct = dct.copy()
    if kwargs:
        for k in kwargs:
            if k in out_dct and (out_dct[k] != kwargs[k]):
                out_dct[k] = kwargs[k]
            elif k not in out_dct:
                out_dct[k] = kwargs[k]
    return out_dct


def main():
    d = {'a': 1, 'b': False}
    print(updated(d, a=1, b=True, c=None))
    print(updated(d) == d)
    print(updated(d) is d)


if __name__ == "__main__":
    main()
