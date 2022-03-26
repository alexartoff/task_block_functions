#!/usr/bin/env python


from operator import add


curry = lambda f: lambda x: lambda y: f(x, y)  # noqa: E731
compose = lambda f: lambda g: lambda x: f(g(x))  # noqa: E731

pair = lambda x: [x, x]  # noqa: E731
dup = lambda x: x + x  # noqa: E731


def enlarge(img_lst):
    # new_img_lst = pair(img_lst)
    print(pair(img_lst))
    print(dup(img_lst))
    # cc = curry(add)(5)
    # print(cc(10), curry(add)(5)(10))


def main():
    # print(enlarge(['+--+', '|x |', '| o|', '+--+',]))
    print(enlarge(['!#', '$@',]))



if __name__ == "__main__":
    main()
