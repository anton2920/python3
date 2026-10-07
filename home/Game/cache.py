import time
import math


def debug(f):
    def wrap(*args, **kwargs):
        start = time.process_time_ns()
        res = f(*args, **kwargs)
        end = time.process_time_ns()

        pos_args_str = ', '.join(map(lambda x: str(x), args))
        kwargs_str = ', '.join([f"{k}={v}" for k, v in kwargs.items()])

        args_str = ""
        if len(args) and len(kwargs):
            args_str = f"{pos_args_str}, {kwargs_str}"
        elif len(kwargs) == 0:
            args_str = pos_args_str
        elif len(args) == 0:
            args_str = kwargs_str

        print(f"""
          {f.name}({args_str})
              Returned: {res}
              Took: {end - start}
        """)
        return res

    return wrap


@debug
def combinations(n, r, algorithm='dumb'):
    if algorithm == 'dumb':
        return dumb_combinations(n, r)
    else:
        return dict_cache_combinations(n, r)


def dumb_combinations(n, r):
    f = lambda x: math.factorial(x)
    r = min(r, n - r)
    return int(f(n) // (f(r) * f(n - r)))


def dict_cache_combinations(base_n, base_r):
    base_r = min(base_r, base_n - base_r)
    cache = {}

    def f(n, r):
        if (r == 0 or n - r == 0):
            return 1
        if (r == 1):
            return n

        i = (n * (base_r - 1)) + r

        if (i not in cache):
            cache[i] = f(n - 1, r) + f(n - 1, r - 1)

        return cache[i]

    return f(base_n, base_r)


def cache(n=-1):
    cache = {}
    def dec(func):
        def wrap(*args):
            if args not in cache:
                res = func(*args)
                if (n > 0) and (len(cache) + 1 > n):
                    del cache[next(iter(cache))]
                cache[args] = res
            return cache[args]
        return wrap
    return dec


@cache(123)
def fib(n):  # 1, 1
    if (n < 1):
        return 0
    if (n == 1):
        return 1

    return fib(n - 2) + fib(n - 1)

print(fib(100))

# combinations(50, 4, algorithm='dumb')
# combinations(50, 4, algorithm='dict')
#
# combinations(900, 800, algorithm='dumb')
# combinations(900, 800, algorithm='dict')


# count = 10
# table = [[(0 if n - r < 0 else dumb_combinations(n, r)) for r in range(count)] for n in range(count)]
#
# i = 0
# for row in [[x for x in range(count)], [], *table]:
#     if (i > 1):
#         print(f"{i - 2}  {" ".join(f"{num:4.0f}" for num in row)}")
#     else:
#         print(f"   {" ".join(f"{num:4.0f}" for num in row)}")
#     i += 1
