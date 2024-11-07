import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://static.realewanderer.net/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Reale"))

def test_get_started_link(page: Page):
    page.goto("https:///static.realewanderer.net/")

    # Click the get started link.
    page.get_by_role("link", name="Website").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="John Reale")).to_be_visible()
