
#try:
    #number = int(input("Введите число: "))
#except ValueError:
    #print("Нужно ввести число.")
#else:
#    print(f"Квадрат числа: {number ** 2}")
#finally:
#    print("Проверка завершена.")

import json
try:
     with open("developer.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        print(data)
except FileNotFoundError:
        print("Файл не найден.")
except json.JSONDecodeError:
        print("Ошибка декодирования JSON.")
else:
    print(data["name"])