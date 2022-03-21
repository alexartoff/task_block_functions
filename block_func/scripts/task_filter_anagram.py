#!/usr/bin/env python


from collections import Counter


def filter_anagrams(source, itrbl):
    s_dict = Counter(source)
    out_itrbl = filter(lambda x: Counter(x) == s_dict, itrbl)
    return out_itrbl


def main():
    print(list(filter_anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])))
    print(list(filter_anagrams('laser', ['lazing', 'lazy',  'lacer'])))


if __name__ == "__main__":
    main()
