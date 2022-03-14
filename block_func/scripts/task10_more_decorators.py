#!/usr/bin/env python


from functools import wraps


def memoizing(memory):
    def memoized(func):
        res_dict = {}
        @wraps(func)
        def inner(x):
            if len(list(res_dict)) > memory:
                res_dict.pop(0)
            if x in res_dict.keys():
                return res_dict[x]
            else:
                res_dict[x] = func(x)
                # print(x, memory, res_dict, res_dict[x])
                return res_dict[x]
        return inner
    return memoized


# @memoizing(3)
# def f(x):
#     print(x, 'Calculating...')
#     return x * 10


arguments = []


@memoizing(3)
def inc(argument):
    arguments.append(argument)
    return argument + 1


def main():
    # f1 = f(1)
    # f2 = f(1)
    # f3 = f(2)
    # f4 = f(3)
    # f5 = f(4)
    # f6 = f(1)
    # print(f1,f2,f3,f4,f5,f6)
    
    print(inc(inc(inc(0))))
    print(arguments)

    print(inc(inc(inc(0))))
    print(arguments)

    print(inc(10))
    print(arguments)
    
    print(inc(0))
    print(arguments)


if __name__ == "__main__":
    main()
