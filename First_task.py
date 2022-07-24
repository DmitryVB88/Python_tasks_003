def summ(num):
    sum = 0
    p = 0
    while num != 0:
        p = num % 10
        sum = sum + p
        num = num // 10
        return sum

print(summ(123))
print(sum)

# print(f'Сумма числа' ,num, '=' ,summ(sum))
