import random
import math
import statistics

# Генерация списка из 100 случайных чисел от 1 до 100
num = [random.randint(1, 100) for _ in range(100)]

# Вычисление статистических показателей
mean = statistics.mean(num)          # Среднее арифметическое
median = statistics.median(num)      # Медиана
stdev = statistics.stdev(num)        # Стандартное отклонение
sqrt_sum = math.sqrt(sum(num))       # Квадратный корень из суммы
r_sqrt = round(sqrt_sum, 2)          # Округление до 2 знаков после запятой

# Вывод результатов
print(f"Среднее: {mean}, Медиана: {median}, Стандартное отклонение: {stdev},Корень из суммы: {r_sqrt}")