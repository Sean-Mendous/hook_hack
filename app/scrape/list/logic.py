import os
import json
import re
from app.logger_setting.logger import logger

def run_flow(input):
    """
    searchword: str
    amount: int
    """
    
    searchword = input["searchword"]
    amount = input["amount"]

    try:
        logger.info(f"extracting urls: {searchword}")
        from app.scrape.list.extract.extract import extract_playwrite
        video_list = extract_playwrite(searchword)
        logger.info(f"success extracting urls: {len(video_list)}")
    except Exception as e:
        raise RuntimeError(f"extracting urls: {e}")
    
    sorted_list = sorted(video_list, key=lambda x: x['like'], reverse=True)
    sorted_list = sorted_list[:amount]

    for i, item in enumerate(sorted_list):
        try:
            match = re.search(r'/video/(\d+)', item['url'])
            id = match.group(1)
            item['id'] = id
            logger.info(f"success extracting id: {id}")
        except Exception as e:
            raise RuntimeError(f"extracting id: {e}")

        try:
            from app.scrape.list.ask.ask import ask
            summary, cloudinary_url = ask(item['url'], item['id'])
            item['analyse'] = summary
            item['storage_url'] = cloudinary_url
            logger.info(f"success summarizing video: {summary}")
        except Exception as e:
            raise RuntimeError(f"summarizing video: {e}")
    
    return sorted_list


if __name__ == "__main__":
    import json
    search_word = '日焼け止め'
    result = run_flow(search_word)
    print(json.dumps(result, indent=4, ensure_ascii=False))

"""
python -m app.scrape.list.logic
""" 

