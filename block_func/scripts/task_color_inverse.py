#!/usr/bin/env python


def to_hex(dgt):
    hex_str = hex(dgt)[2:]
    if len(hex_str) == 1:
        hex_str = '0' + hex_str
    return hex_str


def to_int(hex_str):
    return int(hex_str, 16)


def rgb2hex(r=0, g=0, b=0):
    return f'#{to_hex(r)}{to_hex(g)}{to_hex(b)}'


def hex2rgb(color):
    color_lst = ['r', 'g', 'b']
    color_data = [a+b for a, b in zip(color[1::2], color[2::2])]
    color_data_int = list(map(to_int, color_data))
    return dict(zip(color_lst, color_data_int))


def main():
    print(rgb2hex(36, 171, 0)) #24ab00
    print(rgb2hex(r=36, b=255, g=171)) #24ab00
    print(hex2rgb('#24ab00')) #{'r': 36, 'g': 171, 'b': 0}


if __name__ == "__main__":
    main()
