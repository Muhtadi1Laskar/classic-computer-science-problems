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


print(fib(10))
print(fib_memo(100))