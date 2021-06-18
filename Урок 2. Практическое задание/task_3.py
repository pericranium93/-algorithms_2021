"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены

Используем операции % //, НЕ ИСПОЛЬЗУЕМ ОПЕРАЦИИ ВЗЯТИЯ ЭЛЕМЕНТА ПО ИНДЕКСУ

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321

Не забудьте проверить и на числах, заканчивающихся нулем.
Пример:
Введите число, которое требуется перевернуть: 1230
Перевернутое число: 0321

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def reverse_number(cur_num):
    if cur_num < 10:
        return str(cur_num)
    else:
        return str(cur_num % 10) + reverse_number(cur_num // 10)


def reverse_number_2(cur_num):
    return str(cur_num) if cur_num < 10 else \
        str(cur_num % 10) + reverse_number_2(cur_num // 10)


if __name__ == '__main__':
    while True:
        try:
            number = int(input('Введите натуральное число'))
            if number < 0:
                raise ValueError
            break
        except ValueError:
            print('Недопустимое значение.')

    print(f'Перевернутое число: {reverse_number(number)}')
    print(f'Перевернутое число: {reverse_number_2(number)}')