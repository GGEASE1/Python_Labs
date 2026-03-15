
# Ввод домена
site = input()

# Будем собирать слова и хранить их в списке
parts = []
word = ""

for char in site:
    if char == '.':
        # Если точка, сохраняем накопленное слово
        parts.append(word)
        word = ""
    else:
        word += char
# Добавляем хвост (зону домена)
parts.append(word)

# Выводим части в обратном порядке
i = len(parts) - 1
while i >= 0:
    print(parts[i])
    i -= 1