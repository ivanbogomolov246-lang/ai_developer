goods = input("Название товара: ")
price = float(input("Цена одного товара: "))
quantity = int(input("Количество товара: "))
sale = int(input("Скидка (%): "))
delivery_cost = int(input("Стоимость доставки: "))
cost_no_sale = price * quantity
cost_with_sale = (cost_no_sale / 100) * sale
final_cost = (cost_no_sale - cost_with_sale) + delivery_cost
print(f"Товар: {goods}")
print(f"Количество: {quantity}")
print(f"Стоимость без скидки: {cost_no_sale}")
print(f"Скидка: {cost_with_sale}")
print(f"Доставка: {delivery_cost}")
print(f"Итого: {final_cost:.2f}")