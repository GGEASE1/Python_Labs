prices = list(map(int, input("\nВведите цены через пробел: ").split()))
K = int(input("Введите K: "))
M = int(input("Введите M: "))

discount = [price - (price // K) * M for price in prices]

print("Цены до скидки:", prices)
print("Цены после скидки:", discount)