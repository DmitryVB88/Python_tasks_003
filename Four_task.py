# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Введите число: '))
b = -n
list = []
for i in range (b, n + 1):
    list.append(i)

print(list)


path = r'Four_task_instruction.txt'

with open(path, 'r') as f:
      a = int(f.readline())
      b = int(f.readline())
      c = int(f.readline())
# pr = list[a] * list[a]

print(a, b, c)
pr = list[a] * list[b] * list[c]

print(pr)

      