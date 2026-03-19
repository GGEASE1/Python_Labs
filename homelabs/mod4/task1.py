def check_nums(s):
    # Преобразуем строку в множество чисел (уникальные значения)
    nums = set(map(int, s.split()))
    full_len = len(s.split())
    
    # Логика определения состава чисел
    if len(nums) == 1:
        print("Все числа равны")
    elif len(nums) == full_len:
        print("Все числа разные")
    else:
        print("Есть равные и неравные числа")

check_nums(input())