#!/usr/bin/env python


def decode(code_str):
    lib = (('|_', '1'), ('|¯', '1'), ('_', '0'), ('¯', '0'))
    decode_str = code_str
    for l in lib:
        decode_str = decode_str.replace(*l)
    # tt = map(lambda ss: str.partition(ss, '|_'), code_str)
    # decode_str = map(lambda st, stt: str.replace(st, '|', '1') , code_str)
    return decode_str


def main():
    print(decode('_|¯|____|¯|__|¯¯¯'))


if __name__ == "__main__":
    main()
