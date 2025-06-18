import os
import json
from app.logger_setting.logger import logger

def run_flow(input):
    """
    url: str
    amount: int
    """
    
    url = input["url"]
    amount_output = input["amount"]
    amount_input = 100

    try:
        from app.scrape.indivisual.extract.extract import extract
        comments, datas = extract(url)
    except Exception as e:
        raise RuntimeError(f"extracting comments: {e}")
    
    sorted_comments = sorted(comments, key=lambda x: x['like'], reverse=True)
    for i, comment in enumerate(sorted_comments[:amount_input]):
        comment['number'] = i + 1

    try:
        from app.scrape.indivisual.ask.ask import ask
        label_dict = ask(sorted_comments)
    except Exception as e:
        raise RuntimeError(f"asking comments: {e}")
    
    merged_comments = []
    for comment in comments:
        number = comment["number"]
        if number in label_dict:
            comment_with_label = comment.copy()
            comment_with_label["value"] = label_dict[number]
            merged_comments.append(comment_with_label)

    responce = {}
    responce['datas'] = datas
    responce['comments'] = merged_comments

    return responce

if __name__ == "__main__":
    import json

    url = 'https://www.tiktok.com/@ddden49/video/7094935536153988353'
    
    indivisual_datas = run_flow(url)

    print(f"{json.dumps(indivisual_datas, indent=4, ensure_ascii=False)}")

"""
python -m app.scrape.indivisual.logic
""" 

