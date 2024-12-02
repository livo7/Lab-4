# Словарь предметов: обозначение, размер, очки выживания
items = {
    "r": ("Винтовка", 3, 25),
    "p": ("Пистолет", 2, 15),
    "a": ("Боекомплект", 2, 15),
    "m": ("Аптечка", 2, 20),
    "i": ("Ингалятор", 1, 5),
    "k": ("Нож", 1, 15),
    "x": ("Топор", 3, 20),
    "t": ("Оберег", 1, 25),
    "f": ("Фляжка", 1, 15),
    "d": ("Антидот", 1, 10),
    "s": ("Еда", 2, 20),
    "c": ("Арбалет", 2, 20),
}

# Ограничение по месту в рюкзаке
max_space = 2 * 4  # Предположим, что у Тома 2 строки и 4 столбца в рюкзаке

# Начальные очки выживания и наличие болезни
current_survival_points = 10  # Предполагаем, что у Тома начально 10 очка выживания
has_asthma = False
has_infection = True

# Инициализация матрицы для хранения очков выживания
survival_matrix = [[0 for _ in range(max_space + 1)] for _ in range(len(items) + 1)]

# Заполнение матрицы
for i, item in enumerate(items.values()):
    symbol, size, points = item
    for space in range(max_space + 1):
        if size > space:
            survival_matrix[i + 1][space] = survival_matrix[i][space]
        else:
            survival_matrix[i + 1][space] = max(
                survival_matrix[i][space], survival_matrix[i + 1][space - size] + points
            )

# Получение выбранных предметов
selected_items = []
space = max_space
for i in range(len(items), 0, -1):
    if survival_matrix[i][space] != survival_matrix[i - 1][space]:
        selected_items.append(list(items.keys())[i - 1])
        space -= items[selected_items[-1]][1]

# Отображение выбранных предметов в виде двумерного массива
inventory = [selected_items[i : i + 4] for i in range(0, len(selected_items), 4)]

# Проверка на наличие ингалятора или антидота
if "i" not in selected_items and has_asthma:
    selected_items.append("i")
if "d" not in selected_items and has_infection:
    selected_items.append("d")

# Вывод результата
print("Ивентарь:")
for row in inventory:
    print(row)
print(f"Итоговые очки выживания: {survival_matrix[len(items)][max_space]}")
