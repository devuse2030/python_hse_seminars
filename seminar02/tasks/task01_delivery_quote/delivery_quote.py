def delivery_quote(weight: float, express: bool) -> str:
    if weight <= 1:
        ret = f"{200 * 1.5:.2f}" if express else f"{200:.2f}"
    elif 1 < weight <= 5:
        ret = f"{350 * 1.5:.2f}" if express else f"{350:.2f}"
    elif weight > 5:
        ret = (
            f"{(350 + (weight - 5) * 50) * 1.5:.2f}"
            if express
            else f"{(350 + (weight - 5) * 50):.2f}"
        )
    return f"Доставка: {ret} ₽"
