def pack_batches(weights: list[int], capacity: int) -> list[list[int]]:
    result = []
    current_box = []
    current_weight = 0
    for weight in weights:
        if current_weight + weight <= capacity:
            current_box.append(weight)
            current_weight += weight
        else:
            result.append(current_box)
            current_box = [weight]
            current_weight = weight
    if current_box:
        result.append(current_box)
    return result
