def seat_position(place: int, row_size: int) -> tuple[int, int, bool]:
    seat = (place - 1) % row_size + 1
    return ((place - 1) // row_size + 1, seat, seat == 1 or seat == row_size)
