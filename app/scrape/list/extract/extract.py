from app.logger_setting.logger import logger
from app.scraping_setting.selenium import open_url, login, logout

def extract(search_word, cookie_path='app/scraping_setting/cookies.json'):
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


if __name__ == "__main__":
    import json

    search_word = '日焼け止め'
    result = extract(search_word)
    print(f"success extracting comments: {len(result)}\n")
    print(result)

"""
python -m app.scrape.list.extract.extract
""" 



