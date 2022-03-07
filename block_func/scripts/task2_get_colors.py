#!/usr/bin/env python


def rgb(red=0, green=0, blue=0):
    return 'rgb({}, {}, {})'.format(red, green, blue)


def get_colors():
    out_dct = {
        'red': rgb(red=255),
        'green': rgb(green=255),
        'blue': rgb(blue=255)
        }
    return out_dct


def main():
    colors = get_colors()
    print(set(colors.keys()))
    print(colors['green'])


if __name__ == "__main__":
    main()
