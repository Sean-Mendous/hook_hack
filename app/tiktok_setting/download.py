import os
import yt_dlp
import subprocess

def download(url, output_path, output_filename):
    output_file_path = os.path.join(output_path, output_filename + ".mp4")

    try:
        run_yt_dlp(url, output_file_path)
    except Exception as e:
        raise Exception(f"Error downloading video: {e}")

    try:
        cleaned_output_path = cleanup_videofile(output_file_path)
        return cleaned_output_path
    except Exception as e:
        raise Exception(f"Error cleaning video: {e}")
    finally:
        if os.path.exists(output_file_path):
            os.remove(output_file_path)

def run_yt_dlp(url, output_path):
    ydl_opts = {
        'outtmpl': output_path,
        'format': 'mp4',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def cleanup_videofile(video_path):
    base, ext = os.path.splitext(video_path)
    output_path = f"{base}_cleaned{ext}"

    """
    ・1080p:scale=1920:1080
    ・720p:scale=1280:720
    ・480p:scale=854:480
    ・360p:scale=640:360
    ・240p:scale=426:240
    """

    cmd = [
        "ffmpeg", "-y", "-i", video_path,
        "-vf", "scale=854:480",  # 解像度を指定
        "-vcodec", "libx264",
        "-acodec", "aac",
        "-b:a", "128k",
        "-preset", "veryfast",
        "-movflags", "+faststart",
        output_path
    ]
    subprocess.run(cmd, check=True)

    return output_path

if __name__ == "__main__":
    video_url = "https://www.tiktok.com/@ddden49/video/7094935536153988353"
    download(video_url, "app/tiktok_setting", "video")

"""
python -m app.tiktok_setting.download
"""