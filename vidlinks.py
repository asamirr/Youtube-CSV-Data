import requests
import pandas as pd
from pandas import DataFrame
import sys
from bs4 import BeautifulSoup
from datetime import datetime

time = datetime.now().strftime('_%Y-%m-%d_%H_%M_%S')


channels = ["CHANNEL VIDEOS LINK HERE"] # Example: https://www.youtube.com/user/BBCArabicNews/videos


def pull_video(link):
    r=requests.get(link)
    response= r.text
    soup=BeautifulSoup(response, "html.parser")

    vids = soup.find_all('a')
    videos = []
    for vid in vids:
        v = vid.get("href", "")

        if 'watch' in v:
            videos.append(v)

    return videos

vid_links = []
i = 0

for channel in channels:
    print("Channel {} of {}".format(i+1, len(channels)))
    result = pull_video(channel)
    for r in result:
        if r in vid_links:
            pass
        else:
            vid_links.append(r)


    i = i+1


video_dict = {'video link': vid_links}
df = pd.DataFrame(data=video_dict)
df.head()
print(df, file=sys.stderr)
df.to_csv('CSV_FILE_HERE'.format(time), encoding='utf-8') # Example: "yt.csv"