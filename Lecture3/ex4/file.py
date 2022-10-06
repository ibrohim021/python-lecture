

arr = [i for i in range(10)]

# arr = list(map(lambda x: x%2 == 0, arr))

print(arr)

# Отсортировали элементы по четным
arr = list(filter(lambda x: x%2 == 0, arr))

# Возвели в квадрат и показали кортэж (x, x*2)
arr = list(map(lambda x: (x, x*2), arr))

print(arr)