
list1 = [1,2,3,4,5]

list2 = list1

list1[0] = 45
list2[3] = 99

for i in list1:
    print(i, end='.')

print()

for j in list2:
    print(j, end='.')

print()
print()

print('Удалили элемент с идексом 2')
list1.pop(2)
print(list1)

print()

print('Заменим элемент с идексом 2 на элемент 55')
list1.insert(2, 55)
print(list1)

print('Заменим последний элемент на элемент 55')
list1.append(11)
print(list1)

# arr = [23,343,456,78,8,9]
# count = 0
# for i in range(len(arr)):
#     print(f'Индекс элемента {arr[i]} = {i}')
#     count += 1
# print(f'Кол-во элементов = {count}')