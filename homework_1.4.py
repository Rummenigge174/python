# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
numbers = []
i = 0

user_number = input('Введите число больше 0: ')

while i < len(user_number):
    number = user_number[i]
    numbers.append(number)
    i += 1

print(max(numbers))
