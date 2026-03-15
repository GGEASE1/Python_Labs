def euclid_gcd(a, b):
    """Рекурсивный алгоритм Евклида"""
    if b == 0:
        return a
    # Передаем остаток от деления в следующий вызов
    return euclid_gcd(b, a % b)

n1, n2 = map(int, input().split())
print(euclid_gcd(n1, n2))