N = int(input("\nВведите число N: "))

nums = list(range(N, N**2 + 1))
roots = [x**0.5 for x in nums]

print("Числа:", nums)
print("Квадратные корни:", roots)