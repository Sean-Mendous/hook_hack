import os
import json
from app.logger_setting.logger import logger

def run_flow(url, amount=15):
    responce = {}

    try:
        from app.scrape.indivisual.extract.extract import extract
        comments, datas = extract(url)
    except Exception as e:
        raise RuntimeError(f"extracting comments: {e}")
    
    responce['comments'] = []
    sorted_comments = sorted(comments, key=lambda x: x['like'], reverse=True)
    for i, comment in enumerate(sorted_comments[:amount]):
        commment_data = comment | {'number': i + 1}
        responce['comments'].append(commment_data)
    responce['datas'] = datas

    return responce

if __name__ == "__main__":
    import json

    url = 'https://www.tiktok.com/@ddden49/video/7094935536153988353'
    
    indivisual_datas = run_flow(url)

    print(f"{json.dumps(indivisual_datas, indent=4, ensure_ascii=False)}")

"""
python -m app.scrape.indivisual.logic
""" 

