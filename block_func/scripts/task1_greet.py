#!/usr/bin/env python


def greet(name, *args):
    out_str = f'Hello, {name}'
    if args:
        for item in args:
            out_str += f' and {item}'
    return out_str + '!'


def main():
    print(greet('Alex', 'Bob', 'Sam'))


if __name__ == "__main__":
    main()