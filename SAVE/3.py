# так как мой вариант-3, то мне необходимо брать антидот => его можно не вносить в список всех предметов
items = dict(
    [
        ("r", [25, 3]),
        ("p", [15, 2]),
        ("a", [15, 2]),
        ("m", [20, 2]),
        ("i", [5, 1]),
        ("k", [15, 1]),
        ("x", [20, 3]),
        ("t", [25, 1]),
        ("f", [15, 1]),
        ("c", [20, 2]),
        ("s", [20, 2]),
    ]
)
name_items = list(items.keys())
# так как антидот занимает одно место, то у нас остается 7 ячеек
total_size = 8 - 1

# кол-во очков выживания равно кол-ву стартовых очков + стоимость антидота - стоимость остальных предметов
start_points = 10 + 10 - sum([int(i[0]) for i in items.values()])

# Так как для моего варианта неважно расположение предметов, то мы не обращаем внимание на то, какие они имеют размеры
# обращая внимание лишь на итоговый обьем
accaptable_options = []


def recurs(size_left, i, points, items_taken):
    global items, accaptable_options
    if i == 11 or size_left == 0:
        if points > 0:
            return accaptable_options.append(items_taken)
        else:
            return None
    else:
        if size_left >= items[name_items[i]][1]:
            recurs(
                size_left - items[name_items[i]][1],
                i + 1,
                points + 2 * items[name_items[i]][0],
                items_taken + [name_items[i]],
            )
        recurs(size_left, i + 1, points, items_taken)


recurs(total_size, 0, start_points, ["d"])
for i in accaptable_options:
    print(i)
