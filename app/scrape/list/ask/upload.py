import time
from app.tiktok_setting.download import download
from app.storage_setting.cloudinary import video_to_cloudinary

def upload(url, output_path, id):
    try:
        video_path = download(url, output_path, id)
    except Exception as e:
        raise Exception(f"Error to download video: {e}")

    time.sleep(0.5)

    try:
        cloudinary_url = video_to_cloudinary(video_path)
    except Exception as e:
        raise Exception(f"Error to upload video to cloudinary: {e}")
    
    return cloudinary_url, video_path

if __name__ == "__main__":
    cloudinary_urls = []
    urls = []
    for url in urls:
        cloudinary_url = upload(url)
        cloudinary_urls.append(cloudinary_url)

    print(cloudinary_urls)

"""
python -m app.scrape.list.analyse.upload
"""