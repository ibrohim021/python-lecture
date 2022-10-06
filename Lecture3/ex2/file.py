# Краткое запись list

list = [i for i in range(1, 11) if i%2 == 0]
print(list)

# Добавим функцию возведение в степень

def f(x):
    return x**2

list = [ (i, f(i))  for i in range(1, 11) if i%2 == 0]

print(list)