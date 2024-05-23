from functools import lru_cache

def fib(n: int) -> int:
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

def fib_memo(n: int, memo: dict[int, int] = {}) -> int:
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

@lru_cache(maxsize=None)
def fib_memo_cache(n: int) -> int:
    if n <= 2:
        return 1
    return fib_memo_cache(n-1) + fib_memo_cache(n-2)

print(fib(10))
print(fib_memo(100))
print(fib_memo_cache(100))