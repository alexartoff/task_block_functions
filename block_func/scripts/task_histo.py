#!/usr/bin/env python


from collections import Counter


def histo(lst, min_value = None, max_value = None, bar_char = '#'):
    out_str = ''
    dict_from_lst = dict(Counter(lst))
    min_from_dict = min_value if min_value else min(dict_from_lst.keys())
    max_from_dict = max_value if max_value else max(dict_from_lst.keys())
    # print(dict_from_lst, min_from_dict, max_from_dict)
    for i in range(min_from_dict, (max_from_dict + 1)):
        if i in dict_from_lst.keys():
            out_str += f'{i}|{bar_char * dict_from_lst[i]} {dict_from_lst[i]}\n'
        else:
            out_str += f'{i}|\n'
    return out_str[:-1]


def main():
    # print(histo([1, 1, 3, 4, 5]))
    print(histo([11, 11, 13, 14, 15], min_value = 2, max_value = 4, bar_char = '*'))


if __name__ == "__main__":
    main()
