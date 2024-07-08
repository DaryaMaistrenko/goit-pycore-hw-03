from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []
    
    for user in users:
        # Перетворення дати народження у об'єкт datetime
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        # Зміна року на поточний
        birthday_this_year = birthday.replace(year=today.year)
        
        # Якщо день народження в цьому році вже минув, беремо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        # Перевірка, чи день народження у наступні 7 днів включаючи сьогодні
        if today <= birthday_this_year <= today + timedelta(days=7):
            # Перевірка, чи день народження припадає на вихідний
            if birthday_this_year.weekday() >= 5:  # Субота або неділя
                # Переносимо на наступний понеділок
                while birthday_this_year.weekday() >= 5:
                    birthday_this_year += timedelta(days=1)
            
            # Додаємо користувача та дату привітання до результатів
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })
    
    return upcoming_birthdays

# Приклад використання функції
users = [
    {"name": "Daria Maistrenko", "birthday": "2000.01.12"},
    {"name": "Volodymyr Maistrenko", "birthday": "1974.10.05"},
    {"name": "Tatiana Krasinska", "birthday": "1974.08.17"},
    {"name": "Yurij Krasinsky", "birthday": "1947.07.08"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
# результат: Список привітань на цьому тижні: [{'name': 'Yurij Krasinsky', 'congratulation_date': '2024.07.08'}]