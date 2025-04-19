import array
import random
from datetime import datetime, timedelta


def l_year(year):
#Проверка на високосный год
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def generate_datetime(start_year, years_span):
#Генерация случайной даты и времени
    year = random.randint(start_year, start_year + years_span - 1)

    month_days = [
        31, 29 if l_year(year) else 28, 31, 30, 31, 30,
        31, 31, 30, 31, 30, 31
    ]

    month = random.randint(1, 12)
    day = random.randint(1, month_days[month - 1])


    return datetime(year, month, day)


# Генерируем 10 случайных дат за последние 5 лет
current_year = datetime.now().year
dates = array.array('i', [
    generate_datetime(current_year - 5, 5).toordinal()
    for _ in range(10)
])

# Преобразуем порядковые номера в datetime
datetime_obj = [datetime.fromordinal(ordinal) for ordinal in dates]

# Вычисляем разницу в днях (игнорируя время)
differences = [
    abs((datetime_obj[i + 1] - datetime_obj[i]).days)
    for i in range(len(datetime_obj) - 1)
]

# Выводим результаты
for i, diff in enumerate(differences):
    print(
        f"Разница между {datetime_obj[i].strftime('%Y-%m-%d')} "
        f"и {datetime_obj[i + 1].strftime('%Y-%m-%d')}: {diff} дней"
    )