from tracemalloc import stop


items: dict[str:list] = {
    "r": [3, 25],  # rifle; key = r
    "x": [3, 20],  # axe; key = x
    "p": [2, 15],  # pistol; key = p
    "a": [2, 15],  # ammo; key = a
    "m": [2, 20],  # medkit; key = m
    "s": [2, 20],  # supplies; key = s
    "c": [2, 20],  # crossbow; key = c
    "i": [1, 5],  # inhaler; key = i
    "k": [1, 15],  # knife; key = k
    "t": [1, 25],  # talisman; key = t
    "f": [1, 15],  # flask; key = f
    "d": [1, 10],  # antidot; key = d
}


class Item:
    def __init__(self, key: str):
        self.name: str = key
        self.weight: int = items[key][0]
        self.points: int = items[key][1]

    def __str__(self):
        return self.name


class Inventory:
    def __init__(self, height: int, width: int, difficulty: int):
        self.inventory: list[Item] = []
        self.width = width
        self.capacity = width * height - difficulty
        self.selected_items: list = []

    def add_item(self, item: Item) -> None:
        if self.capacity < item.weight:
            print("Инвентарь полон")
        else:
            self.inventory.append(item)
            self.capacity -= item.weight
            self.selected_items.append(item.name)

    def get_item(self) -> list[str]:
        return self.selected_items

    def __str__(self):
        result = ""
        temp = 0
        for item in self.inventory:
            for _ in range(item.weight):
                if temp == self.width:
                    result += "\n"
                    temp = 0
                result += f"[{item.name}]"
                temp += 1

        return result


def calculate_best_items(inventory_capacity: int) -> list[Item]:
    for key, value in items.items():
        efficiency: float = value[1] / value[0]
        items[key].append(efficiency)
    sorted_items = sorted(items.items(), key=lambda item: item[1][2], reverse=True)

    result: list[Item] = []
    for item in sorted_items:
        if item[1][0] + sum([x.weight for x in result]) <= inventory_capacity:
            result.append(Item(item[0]))
    return result


def select() -> list:
    selected_items: list = []
    for key, value in items.items():
        selected_items.append(key)
    return selected_items


def survival_points(start_points: int, selected_items: list, global_points: list) -> int:
    final_survival_points = (
        start_points
        + sum(items[_][1] for _ in selected_items)
        - (sum(items[_][1] for _ in global_points) - sum(items[_][1] for _ in selected_items))
    )
    return final_survival_points


if __name__ == "__main__":
    print(
        f"Введите сложность, чем выше цыфра тем будет сложнее выжить.)",
    )
    difficulty = int(input())
    inventory = Inventory(2, 4, difficulty)
    [inventory.add_item(item) for item in calculate_best_items(inventory.capacity)]
    print(inventory)
    print(f"Итоговые очки выживания:{survival_points(15, inventory.get_item(), select())}")
