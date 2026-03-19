text = input()
res = ""
length = len(text)

# Проход по строке
for i in range(length):
    # Если текущий символ пробел, значит перед ним была последняя буква слова
    if text[i] == ' ' and i > 0:
        res += text[i-1]

# Добавляем последний символ всей строки (после него пробела нет)
res += text[length-1]

print(res)