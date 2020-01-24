# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

person_time = int(input('Введите время в секундах: '))

# hours = person_time // 3600
# minutes = person_time // 60 - hours * 60
# seconds = person_time - 3600 * hours - 60 * minutes
#
# if hours > 9:
#     hours_high_reg = ''
# else:
#     hours_high_reg = 0

hours = 0
minutes = 0
seconds = 0
zero_hours = ''
zero_minutes = ''
zero_seconds = ''
while True:
    if person_time // 3600 > 0 :
        hours = person_time // 3600
        if hours > 9:
            zero_hours = ''
        else:
            zero_hours = 0
    elif person_time // 60 > 60 * hours:
        minutes = person_time // 60 - hours * 60
        if minutes > 9:
            zero_minutes = ''
        else:
            zero_minutes = 0
    elif person_time - 3600 * hours - 60 * minutes >= 0:
        seconds = person_time - 3600 * hours - 60 * minutes
        if seconds > 9:
            zero_seconds = ''
        else:
            zero_seconds = 0
    break

print(f'{zero_hours}{hours}:{zero_minutes}{minutes}:{zero_seconds}{seconds}')

