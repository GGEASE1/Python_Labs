numbers = list(map(int, input("\nВведите числа через пробел: ").split()))
K = int(input("Введите K: "))

multiples = [x for x in numbers if x % K == 0]

print("Числа, кратные K:", multiples)