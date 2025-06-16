import re
import emoji
import neologdn

def clean(texts):
    cleaned_texts = []
    for text in texts:
        text = remove_specials(text)
        text = convert_full_width(text)
        text = convert_others(text)

        text = re.sub(r'\s+', ' ', text).strip()
        cleaned_texts.append(text)
    
    return cleaned_texts

def remove_specials(text):
    # 絵文字除去（または保持したい場合は別対応）
    text = emoji.replace_emoji(text, replace='')  
    # 記号（感嘆符や絵文字の残骸など）の簡易除去
    text = re.sub(r'[^\w\sぁ-んァ-ン一-龥]', '', text)
    return text

def convert_full_width(text):
    # 半角カナ・全角英数字の正規化
    text = neologdn.normalize(text)
    return text

def convert_others(text):
    # URL除去
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    # ハッシュタグ除去
    text = re.sub(r'#\S+', '', text)
    # メンション（@user）除去
    text = re.sub(r'@\w+', '', text)
    return text

if __name__ == "__main__":
    texts = ['なんか日に日ににこちゃんに似てきてると思うの気のせいかしら。ちゃんみな様可愛いです非常に。', 'ツインテールしたら、性格変わる？？変わらず好きだけど💓💓💓']
    cleaned_texts = clean(texts)
    print(cleaned_texts)

"""
python -m app.analyse.clean
"""
    