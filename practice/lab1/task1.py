N = int(input("Введите количество имен: "))
names = []

for _ in range(N):
    names.append(input("Введите имя: "))

uni = []
lengths = []

for name in names:
    if len(name) not in lengths:
        uni.append(name)
        lengths.append(len(name))

print("Исходный список:", names)
print("Список с уникальной длиной:", uni)