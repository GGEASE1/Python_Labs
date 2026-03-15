def palindrome_maker(s):
    # Словарь частот символов
    cnt = {c: s.count(c) for c in set(s)}
    mid, side = '', ''
    
    # Формирование частей палиндрома
    for c, n in cnt.items():
        if n % 2:
            mid += c
        side += c * (n // 2)
    
    # Если нечетных символов больше 1, палиндром невозможен (можно вывести mid[0] как центр)
    if len(mid) > 1: return 
    print(side + mid + side[::-1])

palindrome_maker(input())