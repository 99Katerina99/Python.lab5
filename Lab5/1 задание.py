import os
import random
import string


def generate_n(length=8):

    """Генерирует случайное имя файла из букв и цифр"""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length)) + '.txt'


def create_f(dir, count=10):
    """Создает случайные файлы в указанной директории"""
    # Создаем директорию, если ее нет
    if not os.path.exists(dir):
        os.makedirs(dir)

    # Создаем файлы и собираем их пути
    f_paths = []
    for _ in range(count):
        filename = generate_n()
        full_path = os.path.join(dir, filename)

        # Создаем пустой файл
        with open(full_path, 'w'):
            pass

        # Получаем абсолютный путь
        abs_path = os.path.abspath(full_path)
        f_paths.append(abs_path)

    return f_paths

# Указываем директорию для создания файлов
target_dir = "random_f"

# Создаем файлы и получаем их абсолютные пути
created_f = create_f(target_dir)

# Выводим абсолютные пути созданных файлов
for f_path in created_f:
    print(f_path)