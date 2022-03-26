#!/usr/bin/env python


import string


valid_str = string.hexdigits + ':'


def is_valid_ipv6(adr):
    if ':' in adr:
        spl = adr.split(':')
        f = filter(lambda x: True if len(x) <= 4 else False, spl)
        print('!', adr, list(f))
        return(adr, True)
    return (adr, False)


def main():
    # print(is_valid_ipv6('1110:d3:2d06:24:400c:5ee0:be:3d')) #True
    print(is_valid_ipv6('2607:G8B0:4010:801::1004')) #False
    print(is_valid_ipv6('000')) #True



if __name__ == "__main__":
    main()
