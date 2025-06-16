from app.logger_setting.logger import logger

def run_flow(comment_text, video_url, user_info):
    video_path = ''
    
    try:
        from app.tiktok_setting.download import download
        status = download(video_url, video_path)
        if not status:
            raise RuntimeError('failed to download video')
    except Exception as e:
        raise RuntimeError(f'download video: {e}')
    
    try:
        from app.llm_setting.gemini import upload_video
        upload_data = upload_video(video_path)
    except Exception as e:
        raise RuntimeError(f'upload video: {e}')
    
    try:
        from app.hook.ask import comment
        about_comment = comment(comment_text, upload_data)
    except Exception as e:
        raise RuntimeError(f'ask comment: {e}')
    
    try:
        from app.hook.ask import hook
        generated_hook = hook(about_comment, user_info)
    except Exception as e:
        raise RuntimeError(f'generate hook: {e}')
    
    return generated_hook
    

