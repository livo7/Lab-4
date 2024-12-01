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
selected_items = {
    "1": (3, 25),  # rifle ip:1
    "2": (3, 20),  # axe ip:2
    "3": (2, 15),  # pistol ip:3
}
selected_items_without_parametrs = []
unselected_items = {
    "4": (2, 15),  # ammo ip:4
    "5": (2, 20),  # medkit ip:5
    "6": (2, 20),  # supplies ip:6
    "7": (2, 20),  # crossbow ip:7
    "8": (1, 5),  # inhaler ip:8
    "9": (1, 15),  # knife ip:9
    "10": (1, 25),  # talisman ip:10
    "11": (1, 15),  # flask ip:11
    "12": (1, 10),  # antidot ip:12
}
flag_rifle = 0
flag_axe = 0
inventory = [["" for _ in range(columns)] for _ in range(lines)]


# показать инвентарь
def show_inventoru():
    for _ in range(lines):
        print(inventory[_])


# доделать


def point_calculator(selected_items, unselected_items):
    survival_points = (
        sum(items[item][1] for item in selected_items)
        - sum(items[item][1] for item in unselected_items)
        + start_survival_points
    )
    return survival_points


def appened_inventori(selected_items):
    if sum(items[item][0] for item in selected_items) <= (lines * columns):
        selected_items_without_parametrs = sorted(list(map(int, selected_items.keys())))
        if "r" in selected_items_without_parametrs:
            flag_rifle = 1
            for _ in range(3):
                inventory[0][_] = "r"
        if "a" in selected_items_without_parametrs:
            flag_axe = 1
            for _ in range(3):
                inventory[1][_] = "a"
        if flag_axe + flag_rifle == 2:
            # and (
            #     "3" in selected_items_without_parametrs
            #     or "4" in selected_items_without_parametrs
            #     or "5" in selected_items_without_parametrs
            #     or "6" in selected_items_without_parametrs
            #     or "7" in selected_items_without_parametrs
            # ):

            if "3" in selected_items_without_parametrs:
                key = "p"
                for _ in range(2):
                    inventory[_][2] = key
            if "4" in selected_items_without_parametrs:
                key = "a"
                for _ in range(2):
                    inventory[_][2] = key
            if "5" in selected_items_without_parametrs:
                key = "m"
                for _ in range(2):
                    inventory[_][2] = key
            if "6" in selected_items_without_parametrs:
                key = "s"
                for _ in range(2):
                    inventory[_][2] = key
            if "7" in selected_items_without_parametrs:
                key = "c"
                for _ in range(2):
                    inventory[_][2] = key

    return inventory


print(appened_inventori(selected_items))
