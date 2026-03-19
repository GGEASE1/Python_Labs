try:
    # Получаем число
    num = int(input())
    
    # Проверка на натуральность
    if num <= 0:
        raise ValueError

    # Функция перевода в систему счисления base
    def convert_base(n, base):
        # ! ВАЖНО: здесь должны быть кавычки
        chars = "0123456789ABCDEF"
        res = ""
        while n > 0:
            # Берем остаток и добавляем соответствующий символ в начало
            res = chars[n % base] + res
            n //= base # Целочисленное деление
        return res

    # Формируем вывод для 2, 8 и 16 систем
    b_val = convert_base(num, 2)
    o_val = convert_base(num, 8)
    h_val = convert_base(num, 16)
    
    print(f"{b_val}, {o_val}, {h_val}")

except ValueError:
    print("Неверный ввод")