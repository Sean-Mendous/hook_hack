import os
import json
from app.logger_setting.logger import logger

def run_flow(searchword, amount=15):
    try:
        logger.info(f"extracting urls: {searchword}")
        from app.scrape.list.extract.extract import extract_playwrite
        result = extract_playwrite(searchword)
        logger.info(f"success extracting urls: {len(result)}")
    except Exception as e:
        raise RuntimeError(f"extracting urls: {e}")
    
    sorted_result = sorted(result, key=lambda x: x['like'], reverse=True)
    sorted_result = sorted_result[:amount]

    for i, item in enumerate(sorted_result):
        item['number'] = i + 1
    
    return sorted_result


if __name__ == "__main__":
    import json
    search_word = '日焼け止め'
    result = run_flow(search_word)
    print(json.dumps(result, indent=4, ensure_ascii=False))

"""
python -m app.scrape.list.logic
""" 

