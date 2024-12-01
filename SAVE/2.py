RED = "\u001b[41m"
BLUE = "\u001b[44m"
END = "\u001b[0m"

# cоздаем словарь с перечнем вещей и их параметрами (размер ячеек, очки выживания)
# у персонажа заражение, так что сразу исключаем антидот ('antidot': (1, 10)) из словаря,
# уменьшаем доступный размер пространства рюкзака на 1 ячейку: 8 - 1 = 7
stuffdict = {
    "rifle": (3, 25),
    "pistol": (2, 15),
    "ammo": (2, 15),
    "medkit": (2, 20),
    "inhaler": (1, 5),
    "knife": (1, 15),
    "axe": (3, 20),
    "talisman": (1, 25),
    "flask": (1, 15),
    "supplies": (2, 20),
    "crossbow": (2, 20),
}

n = len(stuffdict)


def get_size_and_point(stuffdict):
    size = [stuffdict[item][0] for item in stuffdict]
    point = [stuffdict[item][1] for item in stuffdict]
    return size, point


size = get_size_and_point(stuffdict)[1]
ALL_ITEMS_POINTS = sum(x for x in size) + 10  # 10 очков добавили за антидот, которого нет в словаре


def get_memo_table(stuffdict):
    size, point = get_size_and_point(stuffdict)
    M = [[0 for i in range(inv_size + 1)] for j in range(n)]

    for i in range(n):
        for j in range(inv_size + 1):
            if i == 0 or j == 0:
                M[i][j] = 0
            elif size[i] <= j:
                M[i][j] = max(M[i - 1][j], point[i] + M[i - 1][j - size[i]])
            else:
                M[i][j] = M[i - 1][j]
    return M, size, point


def get_selected_items_list(stuffdict):
    M, size, point = get_memo_table(stuffdict)
    res = M[-1][-1]  # макс очков выживания по таблице
    s = inv_size  # начальная вместимость инвентаря
    items_list = []

    for i in range(n - 1, 0, -1):
        if res <= 0:
            break
        if res != M[i - 1][s]:  # если предмет был выбран
            items_list.append((size[i], point[i]))
            res -= point[i]
            s -= size[i]

    selected_stuff = []
    for search in items_list:
        for key, val in stuffdict.items():
            if val == search and key[0] not in selected_stuff:
                selected_stuff += [key[0]] * val[0]
                break
    selected_stuff += ["d"]  # добавляем антидот
    selected_stuff = [
        selected_stuff[i : i + 4] for i in range(0, len(selected_stuff), 4)
    ]  # преобразовали список в массик

    return selected_stuff


if __name__ == "__main__":
    print(f"\n{BLUE}Вариант с инвентарем в 8 ячеек (наличие антидота обязательно):{END}\n")
    inv_size = 7
    max_points_of_survive = (
        get_memo_table(stuffdict)[0][-1][-1] + 10
    )  # c антидотом, ,без 10 начальных очков
    deduct_points = ALL_ITEMS_POINTS - max_points_of_survive  # количество очков вычета
    res_points = max_points_of_survive + 10 - deduct_points  # с учетом первоначальных 10 баллов
    stuff = get_selected_items_list(stuffdict)
    for row in stuff:
        print(" ".join(f"[{item}]" for item in row))
    print(f"\nИтоговые очки выживания: {res_points}\n")

    # для инвентаря размером 7 ячеек
    print(
        f"\n{BLUE}Дополнительный вариант с рюкзаком в 7 ячеек (наличие антидота обязательно):{END} \n"
    )
    inv_size = 6
    max_points_of_survive = (
        get_memo_table(stuffdict)[0][-1][-1] + 10
    )  # c антидотом, ,без 10 начальных очков
    deduct_points = ALL_ITEMS_POINTS - max_points_of_survive  # количество очков вычета
    res_points = max_points_of_survive + 10 - deduct_points  # с учетом первоначальных 10 баллов
    stuff = get_selected_items_list(stuffdict)
    for row in stuff:
        print(" ".join(f"[{item}]" for item in row))
    print(f"\nИтоговые очки выживания: {res_points}\n")

    if res_points > 0:
        print("Поздравляем, вы избежали зомби-ужина! Полный инвентарь — залог выживания!")
    else:
        print(f"{RED}Рюкзак мал, а аппетит у зомби велик. Подумай об этом в следующий раз.{END}")
