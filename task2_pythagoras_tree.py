"""Завдання 2. Рекурсивна візуалізація фрактала «Дерево Піфагора»."""
import math
import matplotlib.pyplot as plt


def add_square(ax, x, y, size, angle, depth):
    """Малює квадрат і рекурсивно додає два квадрати на його верхніх боках."""
    if depth <= 0 or size < 0.5:
        return

    # Нижня сторона квадрата
    dx, dy = size * math.cos(angle), size * math.sin(angle)
    # Перпендикуляр, спрямований угору від основи
    px, py = -dy, dx

    p1 = (x, y)
    p2 = (x + dx, y + dy)
    p3 = (p2[0] + px, p2[1] + py)
    p4 = (p1[0] + px, p1[1] + py)

    polygon = [p1, p2, p3, p4, p1]
    color = plt.cm.YlGn(0.35 + 0.6 * (1 - depth / max_depth))
    ax.fill([p[0] for p in polygon], [p[1] for p in polygon],
            color=color, edgecolor="black", linewidth=0.7)

    # Два дочірні квадрати будуються на сторонах рівнобедреного
    # прямокутного трикутника над поточним квадратом.
    half = size / 2
    apex = (p4[0] + px / 2 + dx / 2, p4[1] + py / 2 + dy / 2)
    # Вершина трикутника зміщена вгору на size/2 від середини даху.
    apex = ((p4[0] + p3[0]) / 2 + px / 2,
            (p4[1] + p3[1]) / 2 + py / 2)

    # Ліва похила сторона: p4 -> apex
    left_dx, left_dy = apex[0] - p4[0], apex[1] - p4[1]
    left_angle = math.atan2(left_dy, left_dx)
    add_square(ax, p4[0], p4[1], math.hypot(left_dx, left_dy),
               left_angle + math.pi / 2, depth - 1)

    # Права похила сторона: apex -> p3
    right_dx, right_dy = p3[0] - apex[0], p3[1] - apex[1]
    right_angle = math.atan2(right_dy, right_dx)
    add_square(ax, apex[0], apex[1], math.hypot(right_dx, right_dy),
               right_angle + math.pi / 2, depth - 1)


if __name__ == "__main__":
    try:
        max_depth = int(input("Вкажіть рівень рекурсії (1–12): "))
        if not 1 <= max_depth <= 12:
            raise ValueError
    except ValueError:
        print("Введіть ціле число від 1 до 12.")
        raise SystemExit(1)

    globals()["max_depth"] = max_depth
    fig, ax = plt.subplots(figsize=(10, 8))
    add_square(ax, -0.5, 0, 1.0, 0, max_depth)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(f"Дерево Піфагора — рівень рекурсії {max_depth}")
    plt.tight_layout()
    plt.show()
