from apiclient.discovery import build
import pandas as pd
import sys
from datetime import datetime

time = datetime.now().strftime('_%Y-%m-%d_%H_%M_%S')

# CREDENTIALS
DEVELOPER_KEY = "YOUR API KEY"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(q, max_results=50,order="relevance", token=None, location=None, location_radius=None):

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
    q=q,
    type="video",
    pageToken=token,
    order = order,
    part="id,snippet",
    maxResults=max_results,
    location=location,
    videoDuration = 'any',
    locationRadius=location_radius).execute()

    title = []
    description = []
    channelId = []
    channelTitle = []
    categoryId = []
    videoId = []
    viewCount = []
    likeCount = []
    dislikeCount = []
    commentCount = []
    favoriteCount = []
    category = []
    tags = []
    videos = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":

            title.append(search_result['snippet']['title'])
            description.append(search_result['snippet']['description'])
            videoId.append(search_result['id']['videoId'])

            response = youtube.videos().list(
                part='statistics, snippet',
                id=search_result['id']['videoId']).execute()
            if 'channelId' in response['items'][0]['snippet'].keys():
                channelId.append(response['items'][0]['snippet']['channelId'])
            if 'channelTitle' in response['items'][0]['snippet'].keys():
                channelTitle.append(response['items'][0]['snippet']['channelTitle'])
            if 'categoryId' in response['items'][0]['snippet'].keys():
                categoryId.append(response['items'][0]['snippet']['categoryId'])
            if 'favoriteCount' in response['items'][0]['statistics'].keys():
                favoriteCount.append(response['items'][0]['statistics']['favoriteCount'])
            if 'viewCount' in response['items'][0]['statistics'].keys():
                viewCount.append(response['items'][0]['statistics']['viewCount'])
            if 'likeCount' in response['items'][0]['statistics'].keys():
                likeCount.append(response['items'][0]['statistics']['likeCount'])
            if 'dislikeCount' in response['items'][0]['statistics'].keys():
                dislikeCount.append(response['items'][0]['statistics']['dislikeCount'])

        if 'commentCount' in response['items'][0]['statistics'].keys():
            commentCount.append(response['items'][0]['statistics']['commentCount'])
        else:
            commentCount.append([])

        if 'tags' in response['items'][0]['snippet'].keys():
            tags.append(response['items'][0]['snippet']['tags'])
        else:
            tags.append([])

    youtube_dict = {'tags': tags, 'channelId': channelId, 'channelTitle': channelTitle,
                    'categoryId':categoryId, 'title': title, 'videoId': videoId,
                    'viewCount': viewCount, 'likeCount': likeCount,
                    'dislikeCount': dislikeCount, 'commentCount': commentCount,
                    'favoriteCount':favoriteCount, 'description': description}

    return youtube_dict


df = pd.read_csv('CSV_FILE_HERE') # Example: "yt.csv"
links = list(df["video link"])
video_data = []
i = 0
for link in links:
    print("Video {} of {}".format(i+1, len(links)))
    results = youtube_search(link)
    video_data.append(results)  
    i = i+1


df = pd.DataFrame(data=video_data)
df.head()
print(df, file=sys.stderr)
df.to_csv('CSV_FILE_HERE'.format(time), encoding='utf-8') # Example: "yt_extracted_data.csv"