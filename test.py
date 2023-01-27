# Test
import time
from playwright.sync_api import sync_playwright

def run(playwright):
    chromium = playwright.chromium
    browser = chromium.launch()
    page = browser.new_page()
    page.goto("https://stundev.github.io/")
    page2 = browser.new_page()
    page2.goto("https://stundev.github.io/")
    time.sleep(300)
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
