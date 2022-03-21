#!/usr/bin/env python


def ip2int(ip_str):
    ip_split = ip_str.split('.')
    ip_int = sum([int(d) * pow(256, i) for i, d in enumerate(ip_split[::-1])])
    # print(128*pow(256, 3) + 32*pow(256, 2) + 10*pow(256, 1) + 1*pow(256, 0))
    return ip_int


def int2ip(ip_dgt):
    if ip_dgt == 0:
        return '0.0.0.0'
    dct = {0: 0, 1: 0, 2: 0, 3: 0}
    for i in range(4):
        dct[i] = (ip_dgt - dct[0] * pow(256, 3) - dct[1] * pow(256, 2) - dct[2] * pow(256, 1)) // pow(256, (len(dct) - 1 - i))
    return f'{dct[0]}.{dct[1]}.{dct[2]}.{dct[3]}'


def main():
    print(ip2int('128.32.10.1')) #2149583361
    print(ip2int('0.0.0.0')) #0
    print(ip2int('0.0.1.1')) #257
    print(int2ip(2149583361)) #'128.32.10.1'
    print(int2ip(257)) #'0.0.1.1'


if __name__ == "__main__":
    main()
