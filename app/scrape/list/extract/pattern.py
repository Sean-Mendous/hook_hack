from bs4 import BeautifulSoup
from app.tiktok_setting.convert_number import k_and_m_into_int

def pattern(html):
    result = []
    soup = BeautifulSoup(html, 'html.parser')
    main_section = soup.find('div', id='main-content-general_search')
    if main_section:
        item_section = main_section.find('div', id='tabs-0-panel-search_top')
        if item_section:
            item_divs = item_section.find_all('div', class_='css-1soki6-DivItemContainerForSearch e19c29qe9')
            for item in item_divs:
                item_dict = {}
                a_tag = item.find('a')
                if a_tag:
                    url = a_tag.get('href')
                    if url:
                        item_dict['url'] = url

                    like = a_tag.find("strong", attrs={"data-e2e": "video-views"})
                    if like:
                        like = k_and_m_into_int(like.text)
                        item_dict['like'] = like

                result.append(item_dict)
    
    return result

