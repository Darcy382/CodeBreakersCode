# Block (a)  // O(n)
sum = 0;
n = N
while n > 0:
    for i in range(0, n):
        sum += 1;
    n = n // 2


# Block (b) // O(nlogn) NOT SURE ABOUT THIS ONE
sum = 0
i = 1
while i < N: // log n
    for j in range(0, i): // O(N)
        sum += 1
    i = i * 2

# Block (c) // O(nlogn)
sum = 0
i = 1
while i < N: // log n
    for j in range(0, N): // n
        sum += 1
    i = i * 2