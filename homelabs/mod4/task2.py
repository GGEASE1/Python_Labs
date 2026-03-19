def fast_pow(a, n):
    """Рекурсивное быстрое возведение в степень"""
    if n == 0:
        return 1
    # Если степень четная, сокращаем задачу вдвое
    if n % 2 == 0:
        return fast_pow(a * a, n // 2)
    # Если нечетная, выносим множитель
    return a * fast_pow(a, n - 1)

base, exp = map(int, input().split())
print(fast_pow(base, exp))