# Считываем строку с числами
raw_data = input()

# Парсинг строки вручную (без split)
nums = []
buffer = ""
for char in raw_data:
    if char == ' ':
        if buffer:
            nums.append(int(buffer)) # Добавляем число в список
            buffer = ""
    else:
        buffer += char
# Добавляем последнее число после цикла
if buffer:
    nums.append(int(buffer))

a, b, c = nums[0], nums[1], nums[2]

# Логика поиска среднего элемента методом исключения
# Проверяем, лежит ли A между B и C
if (b <= a <= c) or (c <= a <= b):
    print(a)
# Проверяем, лежит ли B между A и C
elif (a <= b <= c) or (c <= b <= a):
    print(b)
# Иначе средним является C
else:
    print(c)