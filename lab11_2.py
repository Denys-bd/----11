import json

with open("metals.json", "r", encoding="utf-8") as file:
    prices = json.load(file)

metal = input("Введіть назву металу (золото, срібло, платина): ").lower()
weight = float(input("Введіть масу виробу в грамах: "))

if metal in prices:
    cost = prices[metal] * weight
    print("Вартість виробу:", cost, "грн")
else:
    print("Такого металу немає у файлі.")