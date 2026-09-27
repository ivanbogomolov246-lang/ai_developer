students = {
    "Иван": 78,
    "Анна": 92,
    "Олег": 65,
    "Мария": 88,
    "Пётр": 100
}
count = 0
for key, value in students.items():
    print(f"{key}: {value}")
    if value >= 70:
        count += 1
average_score = sum(students.values()) / len(students) 
print(f"Средний балл: {average_score:.2f}")
print(f"Минимальный балл: {min(students.values())}")
print(f"Максимальный балл: {max(students.values())}")
print(f"Учеников с баллом 70+: {count}")
print(f"Уникальных результатов: {len(set(students.values()))}")
