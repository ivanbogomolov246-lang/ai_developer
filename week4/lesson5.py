import json
from developer_model import Developer
ivan = Developer("Иван", 20, "Python", 1)
print(ivan.get_info())
data = ivan.to_dict()
with open("developer_profile.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

try:
    with open("developer_profile.json", "r", encoding="utf-8") as file:
        loaded_data = json.load(file)
except FileNotFoundError:
    print("Файл не найден")
except json.JSONDecodeError:
    print("Ошибка: файл содержит некорректный JSON.")
else:
    print("Данные успешно загружены")
    print(loaded_data)
    loaded_developer = Developer(
    loaded_data["name"],
    loaded_data["age"],
    loaded_data["language"],
    loaded_data["experience"]
)
    print(loaded_developer.get_info())

print(data)
print(type(data))