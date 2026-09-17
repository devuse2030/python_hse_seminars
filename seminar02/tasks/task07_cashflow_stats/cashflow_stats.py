def cashflow_stats(path: str) -> tuple[int, int, int, int]:
    count = 0
    income = 0
    expenses = 0
    with open(path, encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line == "STOP":
                break
            sign, amount = line.split()
            amount = int(amount)
            count += 1
            if sign == "+":
                income += amount
            else:
                expenses += amount
    return count, income, expenses, income - expenses
