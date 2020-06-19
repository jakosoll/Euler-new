
def check_pyf_triplet(a, b, c):
    """Returns True or False"""
    return (a ** 2) + (b ** 2) == c ** 2


def chech_sum(a, b, c):
    """Returns True or False"""
    return (a + b + c) == 1000


def triple():
    for m in range(2, 50):  # предполагаем, что нужная тройка найдется при m < 50
        if m % 2 == 0:  # если m четное, то начинать генерацию с нечетных и наоборот
            k = 1
        else:
            k = 2
        for n in range(k, m, 2):  # шаг 2 и число, с которого начинается генерация
            # ! формулы для генерации Пифагоровых троек
            x = ((m ** 2) - (n ** 2)) 
            y = ((2 * (m * n)))
            z = (((m ** 2) + (n ** 2)))
            if check_pyf_triplet(x, y, z) and chech_sum(x, y, z):
                return x * y * z

if __name__ == "__main__":
    print(triple())
