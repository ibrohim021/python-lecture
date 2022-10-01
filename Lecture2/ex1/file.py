# color = ['red', 'green', 'blue', 'black']
# data = open('file.txt' , 'w')
# data.writelines(color)
# data.write('\nline1\n')
# data.write('line2')
# data.close()



path = 'file.txt'
data = open(path, 'r')

for line in data:
    print(line)

data.close()