def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


n = 13
i = 6

while not (i == 10001):
    n += 1
    if is_prime(n):
        i += 1
print(n)