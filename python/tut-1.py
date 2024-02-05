from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    chromium = playwright.chromium  # or "firefox" or "webkit".
    browser = chromium.launch()
    page = browser.new_page()
    page.goto("http://example.com")
    # other actions...

    # Capture a screenshot and save it as "example.png"
    page.screenshot(path="example.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)

