#!/usr/bin/env python


def same_parity_filter(lst):
    if not lst:
        return []
    flag = 0 if lst[0] % 2 == 0 else 1
    filter_lst = filter(lambda x: x % 2 == flag, lst)
    return list(filter_lst)


def main():
    print(same_parity_filter([2, 0, 1, -3, 10, -2])) #[2, 0, 10, -2]
    print(same_parity_filter([-1, 0, 1, -3, 10, -2])) #[-1, 1, -3]
    print(same_parity_filter([])) #[]



if __name__ == "__main__":
    main()
