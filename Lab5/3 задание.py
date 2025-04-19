import json
import random
import string


class Generator:
    def __init__(self):
        self.f_n = ["John", "Star", "Mark", "Dgo", "Emy", "Sara", "Robert", "Five"]
        self.l_n = ["Doe", "Smith", "Williams", "Jones", "Miller", "Hargreves"]
        self.domains = ["mail.ru", "gmail.com", "yandex.com", "outlook.com"]
        self.punctuation = "!@#$%^&*()_+-=[]{}|;:,.<>?\"'"

    def password(self, length=12):
        while True:
            password = ''.join(random.choice(string.ascii_letters + string.digits + self.punctuation)
                               for _ in range(length))
            if any(c in self.punctuation for c in password):
                return password

    def name(self):
        return f"{random.choice(self.f_n)} {random.choice(self.l_n)}"

    def email(self, name):
        first, last = name.lower().split()
        variants = [
            f"{first}{last}",
            f"{first}.{last}",
            f"{first[0]}{last}",
            f"{first}{last}{random.randint(1, 9)}"
        ]
        return f"{random.choice(variants)}@{random.choice(self.domains)}"

    def generate_user(self):
        name = self.name()
        age = random.randint(10, 100)
        email = self.email(name)
        password = self.password()

        return {
            "name": name,
            "age": age,
            "email": email,
            "password": password
        }

def save_to_json(data, filename="user.json"):
    json_string = json.dumps(data, indent=4)
    with open(filename, 'w') as f:
        f.write(json_string)  # Запись JSON строки в файл

def load_from_json(filename="user.json"):
    with open(filename, 'r') as f:
        json_string = f.read()  # Чтение JSON строки из файла
    return json.loads(json_string)

# Читаем и выводим
loaded_data = load_from_json()
print("\nДанные пользователя из файла:")
print(json.dumps(loaded_data, indent=4))