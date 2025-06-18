import time
import random

def open_url(url, p):
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(url)
    return browser, page

def login(browser, cookie_path='app/scraping_setting/cookies.json'):
    browser.new_context(storage_state=cookie_path)

def logout(browser, cookie_path='app/scraping_setting/cookies.json'):
    context = browser.new_context()
    context.storage_state(path=cookie_path)
    browser.close()

def scroll_page_human_like(page, max_attempts, same_height_threshold):
    same_height_count = 0
    last_height = page.evaluate("document.body.scrollHeight")

    for attempt in range(max_attempts):
        step = random.randint(300, 1000)
        page.mouse.wheel(0, step)
        time.sleep(random.uniform(1, 3))

        new_height = page.evaluate("document.body.scrollHeight")

        if new_height == last_height:
            same_height_count += 1
        else:
            same_height_count = 0

        last_height = new_height

        if same_height_count >= same_height_threshold:
            break

        print(f"attempt: {attempt}")
    
    html = page.content()
    return html
