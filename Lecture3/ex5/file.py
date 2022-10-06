user = ['dima', 'petya', 'vasya','kiril']
ids = [21, 34, 5,7 ]
solar = [1000, 1200, 1020, 500]

data = list(zip(user, ids, solar))
print(data)

print()

print('Пронумеровали список элементов')
data = list(enumerate(user))
print(data)

