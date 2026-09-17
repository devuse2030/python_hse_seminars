def analyze_scores(scores: list[int]) -> tuple[list[int], bool, bool]:
    return (
        [i for i in scores if 4 <= i <= 10],
        any(i == 10 for i in scores),
        all(0 <= i <= 10 for i in scores),
    )
