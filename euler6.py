def sum_of_square(n):
    if n < 1:
        return n
    else:
        return n ** 2 + sum_of_square(n - 1)


def square_of_sum(n):
    if n < 1:
        return n
    else:
        return n + square_of_sum(n - 1)

print(square_of_sum(100) ** 2 - sum_of_square(100))