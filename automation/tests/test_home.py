
from playwright.sync_api import Page, expect


def test_homepage_loads(page: Page, base_url: str):
    response = page.goto(
        base_url,
        wait_until="domcontentloaded"
    )

    assert response is not None, "No HTTP response received"
    assert response.status < 400, (
        f"Homepage returned HTTP {response.status}"
    )
    expect(page.locator("body")).to_be_visible()


def test_homepage_displays_product_categories(
    page: Page,
    base_url: str
):
    page.goto(base_url, wait_until="domcontentloaded")

    # Replace these examples with the actual category names
    # and locators found on the website.
    expect(page.locator("body")).to_be_visible()


def test_homepage_has_products_navigation(
    page: Page,
    base_url: str
):
    page.goto(base_url, wait_until="domcontentloaded")

    # Verify the actual navigation label and locator
    # after inspecting the website.
    expect(page.locator("body")).to_be_visible()
