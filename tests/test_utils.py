from core.utils import mask_url


def test_mask_url_none():
    assert mask_url(None) == "None"


def test_mask_url_no_password():
    url = "mongodb://localhost:27017/db"
    assert mask_url(url) == url


def test_mask_url_with_password():
    url = "mongodb://user:pass@host:27017/db"
    masked = mask_url(url)
    assert masked.startswith("mongodb://user:****@host:27017/db")
