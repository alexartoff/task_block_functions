#!/usr/bin/env python


def make_module(step = 1):
    return {'inc': lambda x: x + step, 'dec': lambda x: x - step}


def main():
    m = make_module(step=10)
    print(m['inc'](10))
    print(m['dec'](10))


if __name__ == "__main__":
    main()