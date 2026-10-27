import csv

with open("sales.csv", "r", newline="", encoding="utf-8-sig") as file:
    sample = file.read(1024)
    file.seek(0)

    delimiter = ";" if ";" in sample.splitlines()[0] else ","
    reader = csv.DictReader(file, delimiter=delimiter)

    total = 0
    count = 0

    print("Місяць\tОбсяг продажів")

    for row in reader:
        month = row["Місяць"].strip()
        sales = float(row["Продажі"].strip())

        print(f"{month}\t{sales:g}")
        total += sales
        count += 1

    if count > 0:
        print("Сумарний обсяг продажів:", total)
        print("Середній обсяг продажів:", round(total / count, 2))
