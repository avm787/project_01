# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!


months = 'январь, февраль, март, апрель, май, июнь, июль, август, сентябрь, октябрь, ноябрь, декабрь'
day = '31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31'
s = months.split(',')
l = day.split(',') 
 
m = input ('Введите номер месяца: ' )
m = int(m)
if  1 <= m <= 12:
    print('Вы ввели', s[m-1], '.', l[m-1], ' дней', sep = '')
else:
    print('Такого месяца нет!')    
