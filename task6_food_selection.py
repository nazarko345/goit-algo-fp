"""Завдання 6. Жадібний алгоритм і динамічне програмування (0/1 knapsack)."""

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(items, budget):
    """Обирає страви за спаданням калорій на одиницю вартості."""
    selected = []
    total_cost = total_calories = 0
    ranked = sorted(items.items(),
                    key=lambda pair: pair[1]["calories"] / pair[1]["cost"],
                    reverse=True)
    for name, data in ranked:
        if total_cost + data["cost"] <= budget:
            selected.append(name)
            total_cost += data["cost"]
            total_calories += data["calories"]
    return selected, total_cost, total_calories


def dynamic_programming(items, budget):
    """Знаходить оптимальний набір страв, кожну можна взяти не більше одного разу."""
    names = list(items)
    n = len(names)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i, name in enumerate(names, start=1):
        cost = items[name]["cost"]
        calories = items[name]["calories"]
        for capacity in range(budget + 1):
            dp[i][capacity] = dp[i - 1][capacity]
            if cost <= capacity:
                dp[i][capacity] = max(
                    dp[i][capacity],
                    dp[i - 1][capacity - cost] + calories
                )

    selected = []
    capacity = budget
    for i in range(n, 0, -1):
        if dp[i][capacity] != dp[i - 1][capacity]:
            name = names[i - 1]
            selected.append(name)
            capacity -= items[name]["cost"]

    selected.reverse()
    total_cost = sum(items[name]["cost"] for name in selected)
    total_calories = sum(items[name]["calories"] for name in selected)
    return selected, total_cost, total_calories


if __name__ == "__main__":
    try:
        budget = int(input("Введіть бюджет: "))
        if budget < 0:
            raise ValueError
    except ValueError:
        print("Бюджет має бути невід'ємним цілим числом.")
        raise SystemExit(1)

    for title, algorithm in [
        ("Жадібний алгоритм", greedy_algorithm),
        ("Динамічне програмування", dynamic_programming),
    ]:
        selected, cost, calories = algorithm(items, budget)
        print(f"\\n{title}:")
        print("Страви:", ", ".join(selected) if selected else "нічого")
        print(f"Вартість: {cost}; калорійність: {calories}")
