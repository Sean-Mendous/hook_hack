from app.scraping_setting.selenium import open_url, login, logout

def extract(url, cookie_path='app/scraping_setting/cookies.json'):
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


if __name__ == "__main__":
    import json

    url = 'https://www.tiktok.com/@egachannel1/video/7453796980528073992'
    comments, datas = extract(url)
    print(f"success extracting comments: {len(comments)}\n")
    print(f"{json.dumps(datas, indent=4, ensure_ascii=False)}\n")

"""
python -m app.scrape.indivisual.extract.extract
""" 



