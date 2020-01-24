# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

user_number = input('Введите число от 0 до 9: ')
number1 = int(user_number)
number2_str = user_number + user_number
number3_str = user_number + user_number + user_number

summa_numbers = number1 + int(number2_str) + int(number3_str)
print(summa_numbers)