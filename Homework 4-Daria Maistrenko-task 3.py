import re

def normalize_phone(phone_number):
    # Видалення всіх символів, крім цифр та '+'
    phone_number = re.sub(r"\D", "", phone_number)

    # Перевірка чи номер починається з '+'
    if phone_number.startswith('+'):
        # Якщо номер починається з '+', перевіряємо, чи він починається з '+380'
        if not phone_number.startswith('+380'):
            phone_number = '+38' + phone_number[1:]
    else:
        # Якщо номер не починається з '+', додаємо '+38'
        if phone_number.startswith('380'):
            phone_number = '+' + phone_number
        else:
            phone_number = '+38' + phone_number

    return phone_number

# Приклад використання функції
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)