"""Завдання 7. Метод Монте-Карло для кидання двох кубиків."""
import random
from collections import Counter
import matplotlib.pyplot as plt


ANALYTICAL = {
    total: (6 - abs(7 - total)) / 36
    for total in range(2, 13)
}


def monte_carlo_dice_simulation(number_of_rolls=100_000, seed=42):
    if number_of_rolls <= 0:
        raise ValueError("Кількість кидків має бути більшою за нуль.")

    random.seed(seed)
    counts = Counter()
    for _ in range(number_of_rolls):
        dice_sum = random.randint(1, 6) + random.randint(1, 6)
        counts[dice_sum] += 1

    probabilities = {
        total: counts[total] / number_of_rolls
        for total in range(2, 13)
    }
    return counts, probabilities


def show_results(number_of_rolls=100_000):
    counts, probabilities = monte_carlo_dice_simulation(number_of_rolls)
    print(f"Результати для {number_of_rolls:,} кидків:")
    print(f"{'Сума':<8}{'Кількість':<14}{'Монте-Карло':<16}{'Аналітична':<14}")
    for total in range(2, 13):
        print(f"{total:<8}{counts[total]:<14}{probabilities[total] * 100:>7.2f}%"
              f"{'':<8}{ANALYTICAL[total] * 100:>7.2f}%")

    totals = list(range(2, 13))
    mc_values = [probabilities[t] * 100 for t in totals]
    exact_values = [ANALYTICAL[t] * 100 for t in totals]

    x = list(range(len(totals)))
    width = 0.38
    plt.figure(figsize=(10, 6))
    plt.bar([v - width / 2 for v in x], mc_values, width, label="Монте-Карло")
    plt.bar([v + width / 2 for v in x], exact_values, width, label="Аналітична")
    plt.xticks(x, totals)
    plt.xlabel("Сума двох кубиків")
    plt.ylabel("Імовірність, %")
    plt.title("Порівняння ймовірностей: Монте-Карло та аналітичний розрахунок")
    plt.legend()
    plt.grid(axis="y", alpha=0.25)
    plt.tight_layout()
    plt.savefig("dice_probabilities.png", dpi=150)
    plt.show()


if __name__ == "__main__":
    try:
        rolls = int(input("Введіть кількість кидків (наприклад, 100000): "))
        show_results(rolls)
    except ValueError as error:
        print("Помилка:", error)
