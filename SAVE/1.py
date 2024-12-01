from itertools import combinations

# Определяем предметы
items = {
    "r": (3, 25),  # Винтовка
    "p": (2, 15),  # Пистолет
    "a": (2, 15),  # Боекомплект
    "m": (2, 20),  # Аптечка
    "i": (1, 5),  # Ингалятор
    "k": (1, 15),  # Нож
    "x": (3, 20),  # Топор
    "t": (1, 25),  # Оберег
    "f": (1, 15),  # Фляжка
    "d": (1, 10),  # Антидот
    "s": (2, 20),  # Еда
    "c": (2, 20),  # Арбалет
}

# Ограничения
max_cells = 9
required_items = ["i", "d"]  # Обязательные предметы


# Функция для вычисления очков выживания
def calculate_survival_points(selected_items):
    total_points = sum(items[item][1] for item in selected_items)
    return total_points


# Генерируем все возможные комбинации предметов
best_combination = None
max_points = -float("inf")

# Ищем все возможные комбинации с обязательными предметами
for combination in combinations(items.keys(), max_cells):
    if all(req in combination for req in required_items):
        points = calculate_survival_points(combination)
        if points > max_points:
            max_points = points
            best_combination = combination

# Формируем двумерный инвентарь
inventory = [["" for _ in range(3)] for _ in range(3)]
if best_combination:
    for i in range(3):
        for j in range(3):
            if i * 3 + j < len(best_combination):
                inventory[i][j] = best_combination[i * 3 + j]

# Выводим результат
for row in inventory:
    print(row)
print(f"Итоговые очки выживания: {max_points}")
