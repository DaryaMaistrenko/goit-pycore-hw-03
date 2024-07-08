from datetime import datetime

def get_days_from_today(date):

    try:
        # Перетворення рядка дати у об'єкт datetime
        date_obj = datetime.strptime(date, "%Y-%m-%d")

        # Отримання поточної дати
        current_date = datetime.today()

        # Розрахунок різниці між поточною датою та заданою датою
        difference = current_date - date_obj

        # Повернення різниці у днях як ціле число
        return difference.days
    
    except ValueError:
        return "Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'."

# Приклад використання функції
print(get_days_from_today("2000-01-12"))
