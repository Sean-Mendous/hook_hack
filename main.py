from app.logger_setting.logger import logger

comments_path='logs/outputs/all_analysed_comments.json'

system_number = 1

logger.info(f"🔥 starting system {system_number} 🔥")

if system_number == 1:
    search_word = '化粧水'
    try:
        from app.comment.logic import run_flow
        all_analysed_comments = run_flow(search_word, amount=20, file_path=comments_path)
    except Exception as e:
        raise RuntimeError(f"running flow: {e}")
if system_number == 2:
    pass

logger.info(f"🍹 successfully run flow 🍹")
    
    
    
