s = input()
c0 = 0 # Счетчик нулей
c1 = 0 # Счетчик единиц

# Итерация по строке
for char in s:
    if char == '0':
        c0 += 1
    elif char == '1':
        c1 += 1

# Сравнение количеств
if c0 == c1:
    print('yes')
else:
    print('no')