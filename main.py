import json
from app.logger_setting.logger import logger

system_number = [1]
search_word = '化粧水'
search_url = 'https://www.tiktok.com/@ddden49/video/7094935536153988353'

logger.info(f"🔥 starting system {system_number} 🔥")

if 1 in system_number:
    try:
        from app.scrape.list.logic import run_flow
        scrape_list = run_flow(search_word, amount=15)
    except Exception as e:
        raise RuntimeError(f"scrape list: {e}")
    with open('app/logs/outputs/scrape_list.json', 'w') as f:
        json.dump(scrape_list, f, indent=4)
    logger.info(f"successfully scrape list / saved json")
if 2 in system_number:
    try:
        from app.scrape.indivisual.logic import run_flow
        scrape_indivisual = run_flow(search_url, amount=15)
    except Exception as e:
        raise RuntimeError(f"scrape indivisual: {e}")
    with open('app/logs/outputs/scrape_indivisual.json', 'w') as f:
        json.dump(scrape_indivisual, f, indent=4)
    logger.info(f"successfully scrape indivisual / saved json")
if 3 in system_number:
    try:
        from app.generate.hook.logic import run_flow
        generate_hook = run_flow()
    except Exception as e:
        raise RuntimeError(f"generate hook: {e}")
    with open('app/logs/outputs/generate_hook.json', 'w') as f:
        json.dump(generate_hook, f, indent=4)
    logger.info(f"successfully generate hook / saved json")
if 4 in system_number:
    try:
        from app.generate.content.logic import run_flow
        generate_content = run_flow()
    except Exception as e:
        raise RuntimeError(f"generate content: {e}")
    with open('app/logs/outputs/generate_content.json', 'w') as f:
        json.dump(generate_content, f, indent=4)
    logger.info(f"successfully generate content / saved json")

logger.info(f"🍹 successfully run flow 🍹")
    
    
    
