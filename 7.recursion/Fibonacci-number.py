
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

# Bottom up iterative
class Solution:
    '''

    0 1 2 3 4 5 6 7  8
    0 1 1 2 3 6 9 15 24...

    '''

    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        num1 = 0
        num2 = 1
        total = 0
        for i in range(N - 1):
            total = num1 + num2
            num1 = num2
            num2 = total
        return total