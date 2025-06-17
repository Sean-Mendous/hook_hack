import json

def analyse(hook, user_info):
    try:
        with open("app/generate/content/ask/prompt.md", "r") as f:
            prompt = f.read()
            prompt = prompt + '\n## フック\n' + hook + '\n## ユーザー情報\n' + user_info
    except Exception as e:
        raise Exception(f"Error to open prompt: {e}")
    
    try:
        from app.llm_setting.chatgpt import chatgpt_4o
        result = chatgpt_4o(prompt)
    except Exception as e:
        raise Exception(f"Error to analyse comment: {e}")
    
    try:
        from app.llm_setting.format import format_dict
        result = format_dict(result)
    except Exception as e:
        raise Exception(f"Error to format dict: {e}")
    
    return result

if __name__ == "__main__":
    hook = "サッカー部なのに、焼けないって最高！"
    with open("api/user_info_demo.json", "r") as f:
        user_info = json.dumps(f.read())

    result = analyse(hook, user_info)
    print(result)

    with open("app/generate/content/demo.json", "w") as f:
        json.dump(result, f, indent=4, ensure_ascii=False)

"""
python -m app.generate.content.ask.ask
"""