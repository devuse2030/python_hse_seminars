def parse_build_tag(tag: str) -> tuple[str, int, str]:
    text = tag.split("/")
    return (text[0].strip().upper(), int(text[1]), text[2].strip().lower()[:7])
