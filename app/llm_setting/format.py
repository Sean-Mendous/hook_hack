import re
import json

def format_dict(response):
    match = re.search(r"```(?:json)?\s*([\s\S]*?)```", response)
    if match:
        json_str = match.group(1).strip()
    else:
        json_str = response.strip()
    if not json_str:
        raise ValueError("Empty JSON content after cleanup.")
    return json.loads(json_str)