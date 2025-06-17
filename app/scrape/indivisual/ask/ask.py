import json

def analyse(comments):
    try:
        with open("app/scrape/indivisual/analyse/prompt.md", "r") as f:
            prompt = f.read()
            prompt = prompt + json.dumps(comments, indent=4, ensure_ascii=False)
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
    json_path = "app/scrape/indivisual/demo.json"
    with open(json_path, "r") as f:
        data = json.load(f)
    
    comments = data["comments"]
    result_dict = analyse(comments)
    label_dict = {item['number']: item['value'] for item in result_dict}

    merged_comments = []
    for comment in comments:
        number = comment["number"]
        if number in label_dict:
            comment_with_label = comment.copy()
            comment_with_label["value"] = label_dict[number]
            merged_comments.append(comment_with_label)
    
    output_path = "app/scrape/indivisual/demo.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump({"comments": merged_comments}, f, indent=4, ensure_ascii=False)

"""
python -m app.scrape.indivisual.analyse.analyse
"""
