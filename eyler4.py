
def palandim():
    for i in range(999, 900, -1):
        for j in range(999, 900, -1):
            multy = i * j
            first = str(multy)[:3]
            second = str(multy)[:2:-1]
            if first == second:
                return i, j


print(palandim())
