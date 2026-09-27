name = input("Ваше имя: ").strip
budget = int(input("Ваш бюджет на день: "))
food_cost = float(input("Стоимость еды: "))
transport_cost = int(input("Стоимость транспорта: "))
other_cost = float(input("Прочие расходы: "))
total_expenses = food_cost + transport_cost + other_cost
money_left = budget - total_expenses
spent_percent = (total_expenses / budget) * 100
print("===БЮДЖЕТ НА ДЕНЬ===")
print(f"Пользователь: {name}")
print(f"Бюджет: {budget:.2f} руб.")
print(f"Всего потрачено: {total_expenses:.2f} руб.")
print(f"Денег осталось: {money_left:.2f} руб.")
print(f"Потрачено: {spent_percent:.2f} руб. %")
print(f"Общая длина имени: {len(name)}")