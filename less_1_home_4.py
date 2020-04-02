# 4)	Пользователь вводит целое положительное число.
#     Найдите самую большую цифру в числе.
#     Для решения используйте цикл while и арифметические операции.

# number = input('Введите целое положительное число: ')
# x = 0
# for i in number:
#     while int(i) > x:
#         x = int(i)
#
# print(x)



num = int(input('Введите целое положительное число: '))
max_number = num % 10
while num > 10:
    if num % 10 > max_number:
        max_number = num % 10
    num = num // 10
print(max_number)





