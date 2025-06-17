import os
import re

def analyse(url, id):
    try:
        from app.scrape.list.analyse.upload import upload
        cloudinary_url, video_path = upload(url, output_path="app/scrape/list/analyse", id=id)
    except Exception as e:
        raise Exception(f"Error to upload video to cloudinary: {e}")
    
    try:
        from app.llm_setting.gemini import upload_video
        uploaded_file = upload_video(video_path)
    except Exception as e:
        raise Exception(f"Error to upload video to gemini: {e}")
    finally:
        if os.path.exists(video_path):
            os.remove(video_path)
    
    try:
        with open("app/scrape/list/analyse/prompt.md", "r") as f:
            prompt = f.read()
    except Exception as e:
        raise Exception(f"Error to open md file: {e}")
    
    try:
        from app.llm_setting.gemini import gemini_20_flash_with_video
        result = gemini_20_flash_with_video(prompt, uploaded_file)
    except Exception as e:
        raise Exception(f"Error to analyse video: {e}")

    return result, cloudinary_url

if __name__ == "__main__":
    import json

    datas = [
    {
        "tiktok_url": "https://www.tiktok.com/@ddden49/video/7094935536153988353",
        "like": 389000,
        "number": 1
    },
    {
        "tiktok_url": "https://www.tiktok.com/@ayami_yamichan/video/6971361926592924929",
        "like": 237400,
        "number": 2
    },
    {
        "tiktok_url": "https://www.tiktok.com/@tantei_cosme/video/7255979521478823169",
        "like": 122200,
        "number": 3
    },
    {
        "tiktok_url": "https://www.tiktok.com/@yokoyamaamane/video/7123899637299268865",
        "like": 101100,
        "number": 4
    },
    {
        "tiktok_url": "https://www.tiktok.com/@gimihpxgwnx/video/7399960692142525704",
        "like": 66800,
        "number": 5
    },
    {
        "tiktok_url": "https://www.tiktok.com/@nazo111111/video/7233339925830044929",
        "like": 57300,
        "number": 6
    },
    {
        "tiktok_url": "https://www.tiktok.com/@mote_cosme/video/7080858571398745346",
        "like": 53000,
        "number": 7
    },
    {
        "tiktok_url": "https://www.tiktok.com/@shushu_223_/video/7129087684571663618",
        "like": 52800,
        "number": 8
    },
    {
        "tiktok_url": "https://www.tiktok.com/@egachannel1/video/7096065068353293569",
        "like": 48500,
        "number": 9
    },
    {
        "tiktok_url": "https://www.tiktok.com/@karen_beauty02/video/7504999841597099284",
        "like": 48000,
        "number": 10
    },
    {
        "tiktok_url": "https://www.tiktok.com/@1haud/video/7406597185027968264",
        "like": 45500,
        "number": 11
    },
    {
        "tiktok_url": "https://www.tiktok.com/@tsumiki_beauty/video/7099374295180184834",
        "like": 43500,
        "number": 12
    },
    {
        "tiktok_url": "https://www.tiktok.com/@noponopisu2/video/7127214496791137538",
        "like": 41900,
        "number": 13
    },
    {
        "tiktok_url": "https://www.tiktok.com/@nao__belle/video/7377699725698534664",
        "like": 41600,
        "number": 14
    },
    {
        "tiktok_url": "https://www.tiktok.com/@kuraberu_cosme/video/7391460008157842706",
        "like": 37100,
        "number": 15
    }
]

    for data in datas:
        print(f'starting {data["number"]}...')

        url = data["tiktok_url"]
        print(f'url: {url}')
        match = re.search(r'/video/(\d+)', url)
        id = match.group(1)
        print(f'id: {id}')

        result, cloudinary_url = analyse(url, id)
        print(f'result: {result}')
        print(f'cloudinary_url: {cloudinary_url}')

        data["analyse"] = result
        data["storage_url"] = cloudinary_url
        data["id"] = id
        with open('app/scrape/list/demo.json', 'w', encoding='utf-8') as f:
            json.dump(datas, f, ensure_ascii=False, indent=4)
        print(f'saved to demo.json')
        
        print(f'{data["number"]} done! \n')

    # result, cloudinary_url = analyse(url="https://www.tiktok.com/@ddden49/video/7094935536153988353", id="7094935536153988353")
    # print(result)
    # print(cloudinary_url)

"""
python -m app.scrape.list.analyse.analyse
"""