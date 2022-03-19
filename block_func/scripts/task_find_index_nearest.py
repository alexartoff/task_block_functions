#!/usr/bin/env python


def find_index_of_nearest(dgt, lst):
    if not lst:
        return None
    # dif_lst = list(map(lambda d: (d-dgt if d-dgt >= 0 else 0), lst))
    dif_lst = list(map(lambda d: abs(d-dgt), lst))
    return dif_lst.index(min(dif_lst))


def main():
    print(find_index_of_nearest(0, [15, 10, 3, 4])) #2
    print(find_index_of_nearest(12, [15, 10])) #1
    print(find_index_of_nearest(4, [7, 5, 4, 4, 3, 6])) #2
    print(find_index_of_nearest(4, [7, 5, 3, 2])) #1


if __name__ == "__main__":
    main()
