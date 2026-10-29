import os
import pytest


@pytest.fixture(scope="session")
def base_url():
    url = os.environ.get(
        "BASE_URL",
        "https://sarika-trader.onrender.com"
    )

    if not url.startswith(("http://", "https://")):
        raise ValueError(f"Invalid BASE_URL: {url!r}")

    return url.rstrip("/")
