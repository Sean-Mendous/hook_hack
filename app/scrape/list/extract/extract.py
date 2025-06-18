import time
from playwright.sync_api import sync_playwright
from app.logger_setting.logger import logger

def extract_selenium(search_word, cookie_path='app/scraping_setting/cookies.json'):
    from app.scraping_setting.selenium import open_url, login, logout
    url = f'https://www.tiktok.com/search?q={search_word}'
    
    try:
        browser = open_url(url, window_whosh=False)
        login(browser, cookie_path)
    except Exception as e:
        raise RuntimeError(f"open browser: {e}")
    
    try:
        input('press enter..:')
        html = browser.page_source
    except Exception as e:
        raise RuntimeError(f"get html: {e}")
    
    try:
        logout(browser, cookie_path)
    except Exception as e:
        raise RuntimeError(f"close browser: {e}")
    
    try:
        from app.scrape.list.extract.pattern import pattern
        result = pattern(html)
    except Exception as e:
        raise RuntimeError(f"extract comments: {e}")
    
    return result

def extract_playwrite(search_word, cookie_path='app/scraping_setting/cookies.json'):
    from app.scraping_setting.playwrite import open_url, login, logout
    url = f'https://www.tiktok.com/search?q={search_word}'

    with sync_playwright() as p:
        try:
            browser, page = open_url(url, p)
            login(browser, cookie_path)
        except Exception as e:
            raise RuntimeError(f"open browser: {e}")
        
        time.sleep(5)
        
        try:
            from app.scraping_setting.playwrite import scroll_page_human_like   
            html = scroll_page_human_like(page, max_attempts=50, same_height_threshold=5)
        except Exception as e:
            raise RuntimeError(f"get html: {e}")
        
        try:
            logout(browser, cookie_path)
        except Exception as e:
            raise RuntimeError(f"close browser: {e}")
        
    try:
        from app.scrape.list.extract.pattern import pattern
        result = pattern(html)
    except Exception as e:
        raise RuntimeError(f"extract comments: {e}")
    
    return result


if __name__ == "__main__":
    import json
    search_word = '化粧水'
    result = extract_playwrite(search_word)
    print(f"success extracting comments: {len(result)}\n")
    print(result)

"""
python -m app.scrape.list.extract.extract
""" 



