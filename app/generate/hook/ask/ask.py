import json

def ask(comment, video_summary, user_info):
    try:
        with open("app/generate/hook/ask/prompt.md", "r") as f:
            prompt = f.read()
            prompt = prompt + '\n## 動画概要\n' + video_summary + '\n## コメント本文\n' + comment + '\n## ユーザー情報\n' + user_info
    except Exception as e:
        raise Exception(f"Error to open prompt: {e}")
    
    try:
        from app.llm_setting.chatgpt import chatgpt_4omini
        result = chatgpt_4omini(prompt)
    except Exception as e:
        raise Exception(f"Error to analyse comment: {e}")
    
    try:
        from app.llm_setting.format import format_dict
        result = format_dict(result)
    except Exception as e:
        raise Exception(f"Error to format dict: {e}")
    
    return result

if __name__ == "__main__":
    comment = "女子サッカー部の者です。左のやつ時間置いて2回塗るとまじで焼けないです。アネッサと比較しても肌に優しいしコスパが良すぎます。毎日太陽にさらされてるのに肌白いと褒めていただけるので本当にオススメします"
    video_summary = "日焼け止めを20個試した女性が、顔に塗ると肌が白くなるビオレUVアクアリッチの魅力を伝えている。"
    result = ask(comment, video_summary)
    print(result)

"""
python -m app.generate.hook.ask.ask
"""