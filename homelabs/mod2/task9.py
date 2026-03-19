raw_phone = input()
# Разрешенные символы
valid = "0123456789+"
clean_phone = ""

for char in raw_phone:
    # Проверка на вхождение в белый список
    found = False
    for v in valid:
        if char == v:
            found = True
            break
    
    if found:
        clean_phone += char

print(clean_phone)