from urllib.parse import urlencode
import yt_dlp
from threading import Thread
from const import vids

ydl_opts = {'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'}
def download_vid(url,i):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

for v in vids:
    Thread(target=download_vid,args=(v,0)).start()

