from app.logger_setting.logger import logger

def run_flow(input):
    """
    comment: str
    video_summary: str
    user_info: dict
    """
    
    comment = input["comment"]
    video_summary = input["video_summary"]
    user_info = input["user_info"]
    
    try:
        from app.generate.hook.ask.ask import ask
        result = ask(comment, video_summary, user_info)
    except Exception as e:
        raise Exception(f"Error to ask: {e}")
    
    return result
    

