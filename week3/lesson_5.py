text = input("Введите текст: ").strip()
def create_report(text):
    words = text.split()
    word_count = len(words)
    char_count = len(text)
    py_count = text.count("Python")
    report =f"===== ОТЧЁТ =====\nТекст: {text}\n Количество слов: {word_count}\nКоличество символов: {char_count}\nPython встречается: {py_count}\n=================="
    return report
report = create_report(text)
print(report)
with open("text_report.txt", "w", encoding="utf-8") as file:
    file.write(report)