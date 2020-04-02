#3)	Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

months = {1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель', 5: 'май', 6: 'июнь', 7: 'июль', 8: 'август',
          9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'}
months_num = int(input('Введите номер месяца: '))
months = {1: 'зима', 2: 'зима', 12: 'зима',
          3: 'весна', 4: 'весна', 5: 'весна',
          6: 'лето', 7: 'лето', 8: 'лето',
          9: 'осень', 10: 'осень', 11: 'осень'}
print(months.setdefault(months_num))
season = ['зима', 'весна', 'лето', 'осень']
if months_num == 1 or months_num == 2 or months_num == 12:
    print(season[0])
elif months_num == 3 or months_num == 4 or months_num == 5:
    print(season[1])
elif months_num == 6 or months_num == 7 or months_num == 8:
    print(season[2])
elif months_num == 9 or months_num == 10 or months_num == 11:
    print(season[3])



