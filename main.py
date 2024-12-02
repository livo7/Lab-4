from itertools import combinations

# ip size value
items = {
    "1": (3, 25),  # rifle ip:1 key = r
    "2": (3, 20),  # axe ip:2 key = x
    "3": (2, 15),  # pistol ip:3 key = p
    "4": (2, 15),  # ammo ip:4 key = a
    "5": (2, 20),  # medkit ip:5 key = m
    "6": (2, 20),  # supplies ip:6 key = s
    "7": (2, 20),  # crossbow ip:7 key = c
    "8": (1, 5),  # inhaler ip:8 key = i
    "9": (1, 15),  # knife ip:9 key = k
    "10": (1, 25),  # talisman ip:10 key = t
    "11": (1, 15),  # flask ip:11 key = f
    "12": (1, 10),  # antidot ip:12 key = d
}

# cells - 8=2*4
lines = 2
columns = 4
start_survival_points = 15
selected_items = {}

selected_items_without_parametrs = []
unselected_items = {}

inventory = [["" for _ in range(columns)] for _ in range(lines)]


def point_calculator(selected_items, unselected_items):  # функция расчёта баллов
    survival_points = (
        sum(items[item][1] for item in selected_items)
        - sum(items[item][1] for item in unselected_items)
        + start_survival_points
    )
    return survival_points


def selection_of_items(items):
    selected_items_without_parametrs = sorted(list(map(int, selected_items.keys())))


def append_inventory(selected_items):  # функция создания инвенторя
    flag_rifle = 0
    flag_axe = 0
    if sum(items[item][0] for item in selected_items) <= (lines * columns):
        selected_items_without_parametrs = sorted(list(map(int, selected_items.keys())))
        if 1 in selected_items_without_parametrs:
            flag_rifle = 1
        if 2 in selected_items_without_parametrs:
            flag_axe = 1
        # начало с  axe and rifle
        if flag_rifle + flag_axe == 2 and (
            3 in selected_items_without_parametrs
            or 4 in selected_items_without_parametrs
            or 5 in selected_items_without_parametrs
            or 6 in selected_items_without_parametrs
            or 7 in selected_items_without_parametrs
        ):
            for _ in range(3):
                inventory[0][_] = "r"
            for _ in range(3):
                inventory[1][_] = "x"
            if 3 in selected_items_without_parametrs:
                key = "p"
            elif 4 in selected_items_without_parametrs:
                key = "a"
            elif 5 in selected_items_without_parametrs:
                key = "m"
            elif 6 in selected_items_without_parametrs:
                key = "s"
            elif 7 in selected_items_without_parametrs:
                key = "c"
            for _ in range(2):
                inventory[_][3] = key

        elif flag_rifle + flag_axe == 2 and (
            8 in selected_items_without_parametrs
            or 9 in selected_items_without_parametrs
            or 10 in selected_items_without_parametrs
            or 11 in selected_items_without_parametrs
            or 12 in selected_items_without_parametrs
        ):
            flag_position = 0

            if 8 in selected_items_without_parametrs:
                key = "i"
                inventory[flag_position][3] = key
                flag_position = 1

            if 9 in selected_items_without_parametrs:
                key = "k"
                inventory[flag_position][3] = key
                flag_position = 1

            if 10 in selected_items_without_parametrs:
                key = "t"
                inventory[flag_position][3] = key
                flag_position = 1

            if 11 in selected_items_without_parametrs:
                key = "f"
                inventory[flag_position][3] = key
                flag_position = 1

            if 12 in selected_items_without_parametrs:
                key = "d"
                inventory[flag_position][3] = key
                flag_position = 1

        # конец с  axe and rifle

        # начало с  axe or rifle

        if flag_rifle + flag_axe == 1:
            flag_medium_size_item = 0
            flag_position = 0

            if 1 in selected_items_without_parametrs:
                for _ in range(3):
                    inventory[0][_] = "r"

            if 2 in selected_items_without_parametrs:
                for _ in range(3):
                    inventory[0][_] = "x"

            if 3 in selected_items_without_parametrs:
                key = "p"
                if flag_position == 0:
                    flag_medium_size_item = 1
                    flag_position = 1
                    for _ in range(2):
                        inventory[_][3] = key
                elif flag_position == 1:
                    flag_medium_size_item = 2
                    for _ in range(2):
                        inventory[1][_] = key

            if 4 in selected_items_without_parametrs:
                key = "a"
                if flag_position == 0:
                    flag_medium_size_item = 1
                    flag_position = 1
                    for _ in range(2):
                        inventory[_][3] = key
                elif flag_position == 1:
                    flag_medium_size_item = 2
                    for _ in range(2):
                        inventory[1][_] = key

            if 5 in selected_items_without_parametrs:
                key = "m"
                if flag_position == 0:
                    flag_medium_size_item = 1
                    flag_position = 1
                    for _ in range(2):
                        inventory[_][3] = key
                elif flag_position == 1:
                    flag_medium_size_item = 2
                    for _ in range(2):
                        inventory[1][_] = key

            if 6 in selected_items_without_parametrs:
                key = "s"
                if flag_position == 0:
                    flag_medium_size_item = 1
                    flag_position = 1
                    for _ in range(2):
                        inventory[_][3] = key
                elif flag_position == 1:
                    flag_medium_size_item = 2
                    for _ in range(2):
                        inventory[1][_] = key

            if 7 in selected_items_without_parametrs:
                key = "c"
                if flag_position == 0:
                    flag_medium_size_item = 1
                    flag_position = 1
                    for _ in range(2):
                        inventory[_][3] = key
                elif flag_position == 1:
                    flag_medium_size_item = 2
                    for _ in range(2):
                        inventory[1][_] = key

            if 8 in selected_items_without_parametrs:
                key = "i"
                if flag_medium_size_item == 0:
                    if flag_position == 0:
                        flag_position = 1
                        inventory[0][3] = key

                    elif flag_position == 1:
                        flag_position = 2
                        inventory[1][0] = key

                    elif flag_position == 2:
                        flag_position = 1
                        inventory[1][1] = key

                    elif flag_position == 3:
                        flag_position = 4
                        inventory[1][2] = key

                    elif flag_position == 4:
                        inventory[1][3] = key

                if flag_medium_size_item == 1:
                    if flag_position == 1:
                        flag_position = 2
                        inventory[1][0] = key
                    elif flag_position == 2:
                        flag_position = 3
                        inventory[1][1] = key
                    elif flag_position == 3:
                        inventory[1][2] = key

                if flag_medium_size_item == 2:
                    inventory[1][2] = key

            if 9 in selected_items_without_parametrs:
                key = "k"
                if flag_medium_size_item == 0:
                    if flag_position == 0:
                        flag_position = 1
                        inventory[0][3] = key

                    elif flag_position == 1:
                        flag_position = 2
                        inventory[1][0] = key

                    elif flag_position == 2:
                        flag_position = 1
                        inventory[1][1] = key

                    elif flag_position == 3:
                        flag_position = 4
                        inventory[1][2] = key

                    elif flag_position == 4:
                        inventory[1][3] = key

                if flag_medium_size_item == 1:
                    if flag_position == 1:
                        flag_position = 2
                        inventory[1][0] = key
                    elif flag_position == 2:
                        flag_position = 3
                        inventory[1][1] = key
                    elif flag_position == 3:
                        inventory[1][2] = key

                if flag_medium_size_item == 2:
                    inventory[1][2] = key
            if 10 in selected_items_without_parametrs:
                key = "t"
                if flag_medium_size_item == 0:
                    if flag_position == 0:
                        flag_position = 1
                        inventory[0][3] = key

                    elif flag_position == 1:
                        flag_position = 2
                        inventory[1][0] = key

                    elif flag_position == 2:
                        flag_position = 1
                        inventory[1][1] = key

                    elif flag_position == 3:
                        flag_position = 4
                        inventory[1][2] = key

                    elif flag_position == 4:
                        inventory[1][3] = key

                if flag_medium_size_item == 1:
                    if flag_position == 1:
                        flag_position = 2
                        inventory[1][0] = key
                    elif flag_position == 2:
                        flag_position = 3
                        inventory[1][1] = key
                    elif flag_position == 3:
                        inventory[1][2] = key

                if flag_medium_size_item == 2:
                    inventory[1][2] = key
            if 11 in selected_items_without_parametrs:
                key = "f"
                if flag_medium_size_item == 0:
                    if flag_position == 0:
                        flag_position = 1
                        inventory[0][3] = key

                    elif flag_position == 1:
                        flag_position = 2
                        inventory[1][0] = key

                    elif flag_position == 2:
                        flag_position = 1
                        inventory[1][1] = key

                    elif flag_position == 3:
                        flag_position = 4
                        inventory[1][2] = key

                    elif flag_position == 4:
                        inventory[1][3] = key

                if flag_medium_size_item == 1:
                    if flag_position == 1:
                        flag_position = 2
                        inventory[1][0] = key
                    elif flag_position == 2:
                        flag_position = 3
                        inventory[1][1] = key
                    elif flag_position == 3:
                        inventory[1][2] = key

                if flag_medium_size_item == 2:
                    inventory[1][2] = key
            if 12 in selected_items_without_parametrs:
                key = "d"
                if flag_medium_size_item == 0:
                    if flag_position == 0:
                        flag_position = 1
                        inventory[0][3] = key

                    elif flag_position == 1:
                        flag_position = 2
                        inventory[1][0] = key

                    elif flag_position == 2:
                        flag_position = 1
                        inventory[1][1] = key

                    elif flag_position == 3:
                        flag_position = 4
                        inventory[1][2] = key

                    elif flag_position == 4:
                        inventory[1][3] = key

                if flag_medium_size_item == 1:
                    if flag_position == 1:
                        flag_position = 2
                        inventory[1][0] = key
                    elif flag_position == 2:
                        flag_position = 3
                        inventory[1][1] = key
                    elif flag_position == 3:
                        inventory[1][2] = key

                if flag_medium_size_item == 2:
                    inventory[1][2] = key

        # конец с  axe or rifle

        # начало без  axe and rifle
        if flag_rifle + flag_axe == 0:
            flag_position = 0
            flag_medium_size_item = 0

            if 3 in selected_items_without_parametrs:
                key = "p"
                if flag_medium_size_item == 0:
                    flag_medium_size_item = 1
                    for _ in range(2):
                        inventory[_][0] = key

                elif flag_medium_size_item == 1:
                    flag_medium_size_item = 2
                    for _ in range(2):
                        inventory[_][1] = key

                elif flag_medium_size_item == 2:
                    flag_medium_size_item = 3
                    for _ in range(2):
                        inventory[_][2] = key

                elif flag_medium_size_item == 3:
                    for _ in range(2):
                        inventory[_][3] = key
            if 4 in selected_items_without_parametrs:
                key = "a"
                if flag_medium_size_item == 0:
                    flag_medium_size_item = 1
                    for _ in range(2):
                        inventory[_][0] = key

                elif flag_medium_size_item == 1:
                    flag_medium_size_item = 2
                    for _ in range(2):
                        inventory[_][1] = key

                elif flag_medium_size_item == 2:
                    flag_medium_size_item = 3
                    for _ in range(2):
                        inventory[_][2] = key

                elif flag_medium_size_item == 3:
                    for _ in range(2):
                        inventory[_][3] = key
            if 5 in selected_items_without_parametrs:
                key = "m"
                if flag_medium_size_item == 0:
                    flag_medium_size_item = 1
                    for _ in range(2):
                        inventory[_][0] = key

                elif flag_medium_size_item == 1:
                    flag_medium_size_item = 2
                    for _ in range(2):
                        inventory[_][1] = key

                elif flag_medium_size_item == 2:
                    flag_medium_size_item = 3
                    for _ in range(2):
                        inventory[_][2] = key

                elif flag_medium_size_item == 3:
                    for _ in range(2):
                        inventory[_][3] = key
            if 6 in selected_items_without_parametrs:
                key = "s"
                if flag_medium_size_item == 0:
                    flag_medium_size_item = 1
                    for _ in range(2):
                        inventory[_][0] = key

                elif flag_medium_size_item == 1:
                    flag_medium_size_item = 2
                    for _ in range(2):
                        inventory[_][1] = key

                elif flag_medium_size_item == 2:
                    flag_medium_size_item = 3
                    for _ in range(2):
                        inventory[_][2] = key

                elif flag_medium_size_item == 3:
                    for _ in range(2):
                        inventory[_][3] = key
            if 7 in selected_items_without_parametrs:
                key = "c"
                if flag_medium_size_item == 0:
                    flag_medium_size_item = 1
                    for _ in range(2):
                        inventory[_][0] = key

                elif flag_medium_size_item == 1:
                    flag_medium_size_item = 2
                    for _ in range(2):
                        inventory[_][1] = key

                elif flag_medium_size_item == 2:
                    flag_medium_size_item = 3
                    for _ in range(2):
                        inventory[_][2] = key

                elif flag_medium_size_item == 3:
                    for _ in range(2):
                        inventory[_][3] = key

            if 8 in selected_items_without_parametrs:
                key = "i"
                if flag_medium_size_item == 0:
                    if flag_position == 0:
                        flag_position = 1
                        inventory[0][0] = key

                    elif flag_position == 1:
                        flag_position = 2
                        inventory[0][1] = key

                    elif flag_position == 2:
                        flag_position = 3
                        inventory[0][2] = key

                    elif flag_position == 3:
                        flag_position = 4
                        inventory[0][3] = key

                    elif flag_position == 4:
                        flag_position = 5
                        inventory[1][0] = key

                    elif flag_position == 5:
                        flag_position = 6
                        inventory[1][1] = key

                    elif flag_position == 6:
                        flag_position = 7
                        inventory[1][2] = key

                    elif flag_position == 7:
                        inventory[1][3] = key

                elif flag_medium_size_item == 1:
                    if flag_position == 0:
                        flag_position = 1
                        inventory[0][1] = key

                    elif flag_position == 1:
                        flag_position = 2
                        inventory[0][2] = key

                    elif flag_position == 2:
                        flag_position = 3
                        inventory[0][3] = key

                    elif flag_position == 3:
                        flag_position = 4
                        inventory[1][1] = key

                    elif flag_position == 4:
                        flag_position = 5
                        inventory[1][2] = key

                    elif flag_position == 5:
                        inventory[1][3] = key

                elif flag_medium_size_item == 2:
                    if flag_position == 0:
                        flag_position = 1
                        inventory[0][2] = key

                    elif flag_position == 1:
                        flag_position = 2
                        inventory[0][3] = key

                    elif flag_position == 2:
                        flag_position = 3
                        inventory[1][2] = key

                    elif flag_position == 3:
                        inventory[1][3] = key

                elif flag_medium_size_item == 3:
                    if flag_position == 0:
                        flag_position = 1
                        inventory[0][3] = key

                    elif flag_position == 1:
                        inventory[1][3] = key

            if 9 in selected_items_without_parametrs:
                key = "k"
                if flag_medium_size_item == 0:
                    if flag_position == 0:
                        flag_position = 1
                        inventory[0][0] = key

                    elif flag_position == 1:
                        flag_position = 2
                        inventory[0][1] = key

                    elif flag_position == 2:
                        flag_position = 3
                        inventory[0][2] = key

                    elif flag_position == 3:
                        flag_position = 4
                        inventory[0][3] = key

                    elif flag_position == 4:
                        flag_position = 5
                        inventory[1][0] = key

                    elif flag_position == 5:
                        flag_position = 6
                        inventory[1][1] = key

                    elif flag_position == 6:
                        flag_position = 7
                        inventory[1][2] = key

                    elif flag_position == 7:
                        inventory[1][3] = key

                elif flag_medium_size_item == 1:
                    if flag_position == 0:
                        flag_position = 1
                        inventory[0][1] = key

                    elif flag_position == 1:
                        flag_position = 2
                        inventory[0][2] = key

                    elif flag_position == 2:
                        flag_position = 3
                        inventory[0][3] = key

                    elif flag_position == 3:
                        flag_position = 4
                        inventory[1][1] = key

                    elif flag_position == 4:
                        flag_position = 5
                        inventory[1][2] = key

                    elif flag_position == 5:
                        inventory[1][3] = key

                elif flag_medium_size_item == 2:
                    if flag_position == 0:
                        flag_position = 1
                        inventory[0][2] = key

                    elif flag_position == 1:
                        flag_position = 2
                        inventory[0][3] = key

                    elif flag_position == 2:
                        flag_position = 3
                        inventory[1][2] = key

                    elif flag_position == 3:
                        inventory[1][3] = key

                if flag_medium_size_item == 3:
                    if flag_position == 0:
                        flag_position = 1
                        inventory[0][3] = key

                    elif flag_position == 1:
                        inventory[1][3] = key

            if 10 in selected_items_without_parametrs:
                key = "t"
                if flag_medium_size_item == 0:
                    if flag_position == 0:
                        flag_position = 1
                        inventory[0][0] = key

                    elif flag_position == 1:
                        flag_position = 2
                        inventory[0][1] = key

                    elif flag_position == 2:
                        flag_position = 3
                        inventory[0][2] = key

                    elif flag_position == 3:
                        flag_position = 4
                        inventory[0][3] = key

                    elif flag_position == 4:
                        flag_position = 5
                        inventory[1][0] = key

                    elif flag_position == 5:
                        flag_position = 6
                        inventory[1][1] = key

                    elif flag_position == 6:
                        flag_position = 7
                        inventory[1][2] = key

                    elif flag_position == 7:
                        inventory[1][3] = key

                elif flag_medium_size_item == 1:
                    if flag_position == 0:
                        flag_position = 1
                        inventory[0][1] = key

                    elif flag_position == 1:
                        flag_position = 2
                        inventory[0][2] = key

                    elif flag_position == 2:
                        flag_position = 3
                        inventory[0][3] = key

                    elif flag_position == 3:
                        flag_position = 4
                        inventory[1][1] = key

                    elif flag_position == 4:
                        flag_position = 5
                        inventory[1][2] = key

                    elif flag_position == 5:
                        inventory[1][3] = key

                elif flag_medium_size_item == 2:
                    if flag_position == 0:
                        flag_position = 1
                        inventory[0][2] = key

                    elif flag_position == 1:
                        flag_position = 2
                        inventory[0][3] = key

                    elif flag_position == 2:
                        flag_position = 3
                        inventory[1][2] = key

                    elif flag_position == 3:
                        inventory[1][3] = key

                elif flag_medium_size_item == 3:
                    if flag_position == 0:
                        flag_position = 1
                        inventory[0][3] = key

                    elif flag_position == 1:
                        inventory[1][3] = key

            if 11 in selected_items_without_parametrs:
                key = "f"
                if flag_medium_size_item == 0:
                    if flag_position == 0:
                        flag_position = 1
                        inventory[0][0] = key

                    elif flag_position == 1:
                        flag_position = 2
                        inventory[0][1] = key

                    elif flag_position == 2:
                        flag_position = 3
                        inventory[0][2] = key

                    elif flag_position == 3:
                        flag_position = 4
                        inventory[0][3] = key

                    elif flag_position == 4:
                        flag_position = 5
                        inventory[1][0] = key

                    elif flag_position == 5:
                        flag_position = 6
                        inventory[1][1] = key

                    elif flag_position == 6:
                        flag_position = 7
                        inventory[1][2] = key

                    elif flag_position == 7:
                        inventory[1][3] = key

                elif flag_medium_size_item == 1:
                    if flag_position == 0:
                        flag_position = 1
                        inventory[0][1] = key

                    elif flag_position == 1:
                        flag_position = 2
                        inventory[0][2] = key

                    elif flag_position == 2:
                        flag_position = 3
                        inventory[0][3] = key

                    elif flag_position == 3:
                        flag_position = 4
                        inventory[1][1] = key

                    elif flag_position == 4:
                        flag_position = 5
                        inventory[1][2] = key

                    elif flag_position == 5:
                        inventory[1][3] = key

                elif flag_medium_size_item == 2:
                    if flag_position == 0:
                        flag_position = 1
                        inventory[0][2] = key

                    elif flag_position == 1:
                        flag_position = 2
                        inventory[0][3] = key

                    elif flag_position == 2:
                        flag_position = 3
                        inventory[1][2] = key

                    elif flag_position == 3:
                        inventory[1][3] = key

                elif flag_medium_size_item == 3:
                    if flag_position == 0:
                        flag_position = 1
                        inventory[0][3] = key

                    elif flag_position == 1:
                        inventory[1][3] = key

            if 12 in selected_items_without_parametrs:
                key = "d"
                if flag_medium_size_item == 0:
                    if flag_position == 0:
                        flag_position = 1
                        inventory[0][0] = key

                    elif flag_position == 1:
                        flag_position = 2
                        inventory[0][1] = key

                    elif flag_position == 2:
                        flag_position = 3
                        inventory[0][2] = key

                    elif flag_position == 3:
                        flag_position = 4
                        inventory[0][3] = key

                    elif flag_position == 4:
                        flag_position = 5
                        inventory[1][0] = key

                    elif flag_position == 5:
                        flag_position = 6
                        inventory[1][1] = key

                    elif flag_position == 6:
                        flag_position = 7
                        inventory[1][2] = key

                    elif flag_position == 7:
                        inventory[1][3] = key

                elif flag_medium_size_item == 1:
                    if flag_position == 0:
                        flag_position = 1
                        inventory[0][1] = key

                    elif flag_position == 1:
                        flag_position = 2
                        inventory[0][2] = key

                    elif flag_position == 2:
                        flag_position = 3
                        inventory[0][3] = key

                    elif flag_position == 3:
                        flag_position = 4
                        inventory[1][1] = key

                    elif flag_position == 4:
                        flag_position = 5
                        inventory[1][2] = key

                    elif flag_position == 5:
                        inventory[1][3] = key

                elif flag_medium_size_item == 2:
                    if flag_position == 0:
                        flag_position = 1
                        inventory[0][2] = key

                    elif flag_position == 1:
                        flag_position = 2
                        inventory[0][3] = key

                    elif flag_position == 2:
                        flag_position = 3
                        inventory[1][2] = key

                    elif flag_position == 3:
                        inventory[1][3] = key

                elif flag_medium_size_item == 3:
                    if flag_position == 0:
                        flag_position = 1
                        inventory[0][3] = key

                    elif flag_position == 1:
                        inventory[1][3] = key
    # конец без axe and rifle
    # "1": (3, 25),  # rifle ip:1 key = r
    # "2": (3, 20),  # axe ip:2 key = x

    # "3": (2, 15),  # pistol ip:3 key = p
    # "4": (2, 15),  # ammo ip:4 key = a
    # "5": (2, 20),  # medkit ip:5 key = m
    # "6": (2, 20),  # supplies ip:6 key = s
    # "7": (2, 20),  # crossbow ip:7 key = c

    # "8": (1, 5),  # inhaler ip:8 key = i
    # "9": (1, 15),  # knife ip:9 key = k
    # "10": (1, 25),  # talisman ip:10 key = t
    # "11": (1, 15),  # flask ip:11 key = f
    # "12": (1, 10),  # antidot ip:12 key = d

    return f"{inventory[0]}\n{inventory[1]}"


print(append_inventory(selected_items))
