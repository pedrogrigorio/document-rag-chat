def mask_url(url: str | None) -> str:
    """Remove senha da URL para log seguro"""
    if url is None:
        return "None"
    # Ex: mongodb://user:****@host:port/db
    return url.replace(":", ":****@", 1) if "@" in url else url
