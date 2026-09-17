def digital_root_steps(n: int) -> tuple[int, int]:
    str_n = str(n)
    cnt = 0
    while len(str(str_n)) != 1:
        str_n = str(sum(map(int, str_n)))
        cnt += 1
    return int(str_n), cnt
