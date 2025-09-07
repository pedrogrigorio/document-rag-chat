import re


def mask_url(url: str | None) -> str:
    """Remove senha da URL para log seguro"""
    if url is None:
        return "None"

    # Regex: esquema://usuário:senha@resto
    pattern = r"(.*://[^:/]+):[^@]+(@.*)"
    return re.sub(pattern, r"\1:****\2", url)
