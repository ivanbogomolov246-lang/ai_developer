age = int(input("Возраст: "))
ticket = input("Есть билет? (да / нет): ").strip().lower()
invitation = input("Есть приглашение? (да/нет): ").strip().lower()
if age >= 18 and (ticket == "да" or invitation == "да"):
    print("Проход разрешён")
else:
    print("Проход запрешён")
    