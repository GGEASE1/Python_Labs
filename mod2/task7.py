# Ввод формата "строка,символ"
data = input()

# Поиск разделителя
idx = 0
while idx < len(data):
    if data[idx] == ',':
        break
    idx += 1

# Разделение данных
main_str = data[:idx]
target = data[idx+1:] # Искомый символ

count = 0
# Считаем подряд идущие символы с начала
for char in main_str:
    if char == target:
        count += 1
    else:
        break # Прерываем, если последовательность нарушена

print(count)