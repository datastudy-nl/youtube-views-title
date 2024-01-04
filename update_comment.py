import pickle
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import dotenv, os

dotenv.load_dotenv()


YOUTUBE_CHANNEL_ID = os.getenv('YOUTUBE_CHANNEL_ID')
COMMENT_ID = os.getenv('COMMENT_ID')
SECRET_FILE_PATH = './auth/client_secrets.json'

PICKLE_FILE_PATH = f'./auth/pickles/{YOUTUBE_CHANNEL_ID}.pickle'
if not os.path.exists('./auth/pickles'): os.mkdir('./auth/pickles')
if not os.path.exists(SECRET_FILE_PATH): raise FileNotFoundError(f'{SECRET_FILE_PATH} not found')
if not os.path.exists(PICKLE_FILE_PATH):
    flow = InstalledAppFlow.from_client_secrets_file(SECRET_FILE_PATH, ['https://www.googleapis.com/auth/youtube.force-ssl'])
    cred = flow.run_local_server()
    with open(PICKLE_FILE_PATH, 'wb') as pickle_file: pickle.dump(cred, pickle_file)

with open(PICKLE_FILE_PATH, 'rb') as pickle_file: credentials = pickle.load(pickle_file)

service = build('youtube', 'v3', credentials=credentials)
video_details = service.commentThreads().list(part='snippet', id=COMMENT_ID).execute()['items'][0]['snippet']

if not video_details: raise Exception('No video details found')
like_count = video_details['topLevelComment']['snippet']['likeCount']
reply_count = video_details['totalReplyCount']

old_title = video_details['topLevelComment']['snippet']['textOriginal']
new_title = f"This comment currently has {like_count} likes and {reply_count} replies! \n\nView the sourcecode over at: https://github.com/datastudy-nl/youtube-views-title"

comment_snippet = service.comments().list(part='snippet', id=COMMENT_ID).execute()['items'][0]['snippet']

if old_title != new_title:
    video_details['topLevelComment']['snippet']['textOriginal'] = new_title

    print(new_title)
    service.comments().update(
        part='snippet',
        body={
            'id': COMMENT_ID,
            'snippet': video_details['topLevelComment']['snippet']
        }
    ).execute()