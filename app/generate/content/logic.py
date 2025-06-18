from app.logger_setting.logger import logger

def run_flow(input):
    """
    hook: str
    user_info: dict
    """
    
    hook = input["hook"]
    user_info = input["user_info"]
    
    try:
        from app.generate.content.ask.ask import ask
        result = ask(hook, user_info)
    except Exception as e:
        raise Exception(f"Error to ask: {e}")
    
    return result
    

