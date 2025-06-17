import time
from playwright.sync_api import sync_playwright

def extract_selenium(url, cookie_path='app/scraping_setting/cookies.json'):
    from app.scraping_setting.selenium import open_url, login, logout
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
        from app.scrape.indivisual.extract.pattern import indivisdual_pattern_comments_1, indivisdual_pattern_comments_2
        comments = indivisdual_pattern_comments_1(html)
    except Exception as e:
        raise RuntimeError(f"extract comments: {e}")
    
    try:
        from app.scrape.indivisual.extract.pattern import indivisdual_pattern_datas
        datas = indivisdual_pattern_datas(html)
    except Exception as e:
        raise RuntimeError(f"extract datas: {e}")
    
    return comments, datas

def extract_playwrite(url, cookie_path='app/scraping_setting/cookies.json'):
    from app.scraping_setting.playwrite import open_url, login, logout
    with sync_playwright() as p:
        try:
            browser, page = open_url(url, p)
            login(browser, cookie_path)
        except Exception as e:
            raise RuntimeError(f"open browser: {e}")
        
        time.sleep(5)
        input()
        
        try:
            from app.scraping_setting.playwrite import action
            html = action(page, max_attempts=20, same_height_threshold=3)
        except Exception as e:
            raise RuntimeError(f"get html: {e}")
        
        try:
            logout(browser, cookie_path)
        except Exception as e:
            raise RuntimeError(f"close browser: {e}")
        
    try:
        from app.scrape.indivisual.extract.pattern import indivisdual_pattern_comments_1, indivisdual_pattern_comments_2
        comments = indivisdual_pattern_comments_1(html)
    except Exception as e:
        raise RuntimeError(f"extract comments: {e}")
    
    try:
        from app.scrape.indivisual.extract.pattern import indivisdual_pattern_datas
        datas = indivisdual_pattern_datas(html)
    except Exception as e:
        raise RuntimeError(f"extract datas: {e}")
    
    return comments, datas


if __name__ == "__main__":
    import json

    url = 'https://www.tiktok.com/@mei_ama/video/7508290843829161234'
    comments, datas = extract_playwrite(url)
    print(f"success extracting comments: {len(comments)}\n")
    print(f"{json.dumps(comments, indent=4, ensure_ascii=False)}\n")
    print(f"{json.dumps(datas, indent=4, ensure_ascii=False)}\n")

"""
python -m app.scrape.indivisual.extract.extract
""" 



