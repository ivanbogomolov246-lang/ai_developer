text = "   Я изучаю Python и хочу стать Python Developer   "
print(f"Исходный текст: {text}")
print(f"Без лишних пробелов: {text.strip()}")
print(f"После замены: {text.replace("Python Developer", "AI Developer").strip()}")
print(f"Количество символов после очистки: {len(text.strip())}")