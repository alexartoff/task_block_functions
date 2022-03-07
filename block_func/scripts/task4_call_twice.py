#!/usr/bin/env python


def push_and_count(target, *, value):
    target.append(target)
    return len(target)


def shoot():
    return 'Bang!'


def call_twice_t(function, *args, **kwargs):
    result1 = function(*args, **kwargs)
    result2 = function(*args, **kwargs)
    return result1, result2


def call_twice(fnc, *args, **kwargs):
    if args and kwargs:
        txt_one = fnc(*args, value=kwargs.values)
        txt_two = fnc(*args, value=kwargs.values)
    else:
        txt_one = fnc()
        txt_two = fnc()
    return (txt_one, txt_two)


def main():
    print(call_twice(push_and_count, [], value=42))
    print(call_twice(shoot))


if __name__ == "__main__":
    main()
