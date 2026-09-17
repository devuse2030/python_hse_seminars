def longest_plateau(values: list[int]) -> tuple[int, int]:
    if not values:
        return (-1, 0)
    current_start = 0
    current_len = 1
    best_start = 0
    best_len = 1
    for i in range(1, len(values)):
        if values[i] == values[i - 1]:
            current_len += 1
        else:
            current_start = i
            current_len = 1
        if current_len > best_len:
            best_start = current_start
            best_len = current_len
    return (best_start, best_len)
