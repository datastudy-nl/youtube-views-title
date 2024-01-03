import pickle
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow


YOUTUBE_CHANNEL_ID = 'your-youtube-channel-id'
VIDEO_ID = 'your-video-id'
SECRET_FILE_PATH = './auth/client_secrets.json'

PICKLE_FILE_PATH = f'./auth/pickles/{YOUTUBE_CHANNEL_ID}.pickle'
if not os.path.exists('./auth/pickles'): os.mkdir('./auth/pickles')
if not os.path.exists(SECRET_FILE_PATH): raise FileNotFoundError(f'{SECRET_FILE_PATH} not found')
if not os.path.exists(PICKLE_FILE_PATH):
    flow = InstalledAppFlow.from_client_secrets_file(SECRET_FILE_PATH, ['https://www.googleapis.com/auth/youtube'])
    cred = flow.run_local_server()
    with open(PICKLE_FILE_PATH, 'wb') as pickle_file: pickle.dump(cred, pickle_file)

with open(PICKLE_FILE_PATH, 'rb') as pickle_file: credentials = pickle.load(pickle_file)

service = build('youtube', 'v3', credentials=credentials)
video_details = service.videos().list(part='snippet,statistics', id=VIDEO_ID).execute()['items'][0]
statistics = video_details['statistics']

if video_details:
    views = int(statistics['viewCount'])
    likes = int(statistics['likeCount'])
    dislikes = int(statistics['dislikeCount'])
    comments = int(statistics['commentCount'])
    video_details['snippet']['title'] = f"This video currently has {statistics['viewCount']} views"
    video_details['snippet']['description'] = f"The title should update with your view ;)\n\nThis video currently has {statistics['likeCount']} likes, {statistics['dislikeCount']} dislikes, and {statistics['commentCount']} comments. \n\n#scorchai #scorchchamp #live"

    print(video_details['snippet']['title'])
    service.videos().update(
        part='snippet',
        body={
            'id': VIDEO_ID,
            'snippet': video_details['snippet']
        }
    ).execute()
