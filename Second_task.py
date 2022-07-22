

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n -1)
         
num = int(input('Введите число: '))

list = []
for e in range(1, num + 1):
    list.append(factorial(e))

 
print(f"Произведения чисел от 1 до {num}:  {list}")  

