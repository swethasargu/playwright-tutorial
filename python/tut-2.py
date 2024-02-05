from playwright.sync_api import sync_playwright, Playwright

def test_github_page_title(url, expected_title):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        # Navigate to the specified URL
        page.goto(url)

        # Get the title of the page
        actual_title = page.title()
        page.screenshot(path="image.png")

        # Check if the title matches the expected value
        if actual_title != expected_title:
            print(f"Test Failed: Expected title to be '{expected_title}', but got '{actual_title}'")
            browser.close()
            exit(1)  # Exit with a non-zero status code to indicate test failure

        print("Test Passed: Title is correct!")

        # Close the browser
        browser.close()

# URL to test
github_url = "https://github.com/swethasargu"

# Expected title
expected_title = "swethasargu"

# Run the test
test_github_page_title(github_url, expected_title)
