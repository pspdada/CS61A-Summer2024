def count(f):

    def counted(n):
        counted.call_count += 1
        return f(n)

    counted.call_count = 0
    return counted


def memo(f):
    cache = {}

    def memorized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]

    return memorized


@count
@memo
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


fib(5)
print(fib.call_count)  # 9 = 6 + 3
