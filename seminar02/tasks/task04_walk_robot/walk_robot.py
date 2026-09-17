def walk_robot(commands: list[str]) -> tuple[int, int, int]:
    cnt = 0
    x, y = 0, 0
    for command in commands:
        match command.split():
            case ["left", n]:
                x -= int(n)
                cnt += 1
            case ["right", n]:
                cnt += 1
                x += int(n)
            case ["up", n]:
                cnt += 1
                y += int(n)
            case ["down", n]:
                cnt += 1
                y -= int(n)
            case ["stop"]:
                break
            case ["pause"]:
                continue
    return (x, y, cnt)
