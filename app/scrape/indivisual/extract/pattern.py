from bs4 import BeautifulSoup
from app.tiktok_setting.convert_number import k_and_m_into_int

def indivisdual_pattern_comments_1(html):
    soup = BeautifulSoup(html, 'html.parser')
    comments = []
    groups = soup.find_all('div', class_='css-1k8xzzl-DivCommentContentWrapper e1970p9w2')
    for group in groups:
        name_div = group.find('div', class_='css-1e5c5r0-DivCommentHeaderWrapper e1970p9w3')
        if name_div:
            p_tag = name_div.find('p')
            if p_tag:
                name = p_tag.text

        other_div = group.find('div', class_='css-1ivw6bb-DivCommentSubContentSplitWrapper e1970p9w5')
        if other_div:
            like_div = other_div.find('div', class_='css-1nd5cw-DivLikeContainer edeod5e0')
            if like_div:
                span_tag = like_div.find('span')
                if span_tag:
                    like = k_and_m_into_int(span_tag.text)

        text_span = group.find('span')
        if text_span:
            p_tag = text_span.find('p')
            if p_tag:
                text = p_tag.text

        comments.append({
            'name': name if 'name' in locals() else None,
            'like': like if 'like' in locals() else None,
            'text': text if 'text' in locals() else None
        })

    return comments

def indivisdual_pattern_comments_2(html):
    comments = []
    soup = BeautifulSoup(html, 'html.parser')
    groups = soup.find_all('div', class_='css-1i7ohvi-DivCommentItemContainer eo72wou0')
    for group in groups:
        name_div = group.find('div', class_='css-1mf23fd-DivContentContainer e1g2efjf1')
        if name_div:
            name = name_div.find('span').text

        like_div = group.find('div', class_='css-1iv126k-DivLikeWrapper ezxoskx0')
        if like_div:
            like = like_div.find('span').text
            like = k_and_m_into_int(like)

        text_span = group.find('div', class_='css-1mf23fd-DivContentContainer e1g2efjf1')
        if text_span:
            text = text_span.find('p').text

        comments.append({
            'name': name if 'name' in locals() else None,
            'like': like if 'like' in locals() else None,
            'text': text if 'text' in locals() else None
        })

    return comments

def indivisdual_pattern_datas(html):
    datas = {}
    soup = BeautifulSoup(html, 'html.parser')

    main_div = soup.find('div', id='main-content-video_detail')
    if not main_div:
        return datas

    action_containers = main_div.find_all('div', class_='css-1npmxy5-DivActionItemContainer er2ywmz0')
    if not action_containers:
        return datas

    for container in action_containers:
        buttons = container.find_all('button')
        for button in buttons:
            span_tag = button.find('span')
            strong_tag = button.find('strong')

            if not span_tag or not strong_tag:
                continue

            data_e2e = span_tag.get('data-e2e')
            count_text = strong_tag.text.strip()

            if not count_text:
                continue

            if data_e2e == "like-icon":
                key = "likes"
            elif data_e2e == "comment-icon":
                key = "comments"
            elif data_e2e == "undefined-icon": #saves
                key = "saves"
            elif data_e2e == "share-icon":
                key = "shares"
            else:
                continue

            datas[key] = k_and_m_into_int(count_text)
               
    return datas