
# Top down recursive solution using memorization

def fib(self, N: int) -> int:
    memo = {}
    return self._fib(N, memo)


def _fib(self, N, memo):
    if N < 0:
        return
    elif N == 0:
        return 0
    elif N == 1:
        return 1
    elif N not in memo:
        memo[N] = self._fib(N - 1, memo) + self._fib(N - 2, memo)
    return memo[N]