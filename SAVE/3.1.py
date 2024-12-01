# Сохраним условия моего варианта и проверим возможность найти решение при обьеме равном 7-1(из-за необходмости взять антидот)
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

total_size = 7 - 1


start_points = 10 + 10 - sum([int(i[0]) for i in items.values()])


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
                size_left - items[name_items[i]][1], i + 1, points + 2 * items[name_items[i]][0], items_taken + [name_items[i]]
            )
        recurs(size_left, i + 1, points, items_taken)


recurs(total_size, 0, start_points, ["d"])
for i in accaptable_options:
    print(i)
# Заметим, что функция ничего не выводит => невозможно выбрать предметы для рюкзака обьемом 7 единиц так, чтобы выполнялись условия
# Проверим еще раз, но более точечно возможно ли найти набор, удовлетворяющий условиям
all_items = []
total_size = 7 - 1
points = 10 + 10 - sum([int(i[0]) for i in items.values()])

for i in range(11):
    all_items.append([name_items[i], *items[name_items[i]]])
all_items.sort(key=lambda f: f[1] / f[2], reverse=True)

i = 0
while total_size != 0:
    if total_size - all_items[i][2] >= 0:
        total_size -= all_items[i][2]
        points += 2 * all_items[i][1]
    i += 1
if points >= 0:
    print("Possible")
else:
    print("Impossible")
# Так как программа выводит второй вариант, то такой набор найти нельзя при таких вводных данных
