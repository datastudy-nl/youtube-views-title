# YouTube Video Details Updater

<p align="center">
    <img src="https://raw.githubusercontent.com/datastudy-nl/.github/main/assets/datastudy-gh.png" alt="DataStudy Logo">
    <br><i>A datastudy project</i>
</p>

This repository contains code to automatically update YouTube video details using the YouTube Data API v3. It updates the video's title and description with the latest statistics like view count, like count, dislike count, and comment count.

## Prerequisites

- Python 3.6 or higher
- Google account with YouTube Data API v3 enabled
- `google-auth`, `google-auth-oauthlib`, and `google-auth-httplib2` libraries

## Setup and Installation

1. **Google API Console Configuration:**
    - Go to the Google API Console and create a new project.
    - Enable the YouTube Data API v3 for your project.
    - Create credentials for a Desktop app.
    - Download the client secret JSON file.

2. **Environment Setup:**
    - Clone the repository: `git clone https://github.com/datastudy-nl/youtube-views-title.git`
    - Install required libraries: `pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`

3. **Configuration:**
    - Replace `'your-youtube-channel-id'` and `'your-video-id'` in the script with your actual YouTube channel ID and video ID.
    - Place your downloaded client secrets JSON file in the `./auth/` directory and update its path in the script.

## Usage

Run the script with Python:

```bash
python3 update_title.py
```
