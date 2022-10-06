# def select(f, col):
#     return [f(x) for x in col]

# def wher(f, col):
#     return [x for x in col if f(x)]

# arr = '1 2 3 4 5 6'.split()

# # print(arr)

# res = select(int, arr)
# res = wher(lambda x: not x % 2, res)
# print(res)
# res = select(lambda x: (x, x**2), res)
# print(res)

# arr = [i for i in range(1,11)]
# print(arr)

# print()

# print('увеличим элементы списка на 10')

# arr = list(map(lambda x: x+10, arr))

# print(arr)

# Создаем список элементы вводим с клавиатуры

data = list(map(int,input('Введите число: ').split()))
print(data)

