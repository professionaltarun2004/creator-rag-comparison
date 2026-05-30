'''
This file is responsible for:

extracting structured metadata from social media videos.

This includes:

title
creator/uploader
views
likes
comments
upload date
duration
hashtags/tags

This metadata becomes:

business intelligence layer for your RAG system.
'''

import yt_dlp

def get_youtube_metadata(url:str):
    
    ydl_opts={
        "quiet":True,
        "skip_download":True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info=ydl.extract_info(url,download=False)
        views=info.get("view_count",0)
        likes = info.get("like_count", 0)
        comments = info.get("comment_count", 0)

        engagement_rate=0
        if views>0:
            engagement_rate=(
                (likes+comments)/views
            )*100

        metadata = {
            "video_id": info.get("id"),
            "platform": "youtube",
            "title": info.get("title"),
            "creator": info.get("uploader"),
            "views": views,
            "likes": likes,
            "comments": comments,
            "duration": info.get("duration"),
            "upload_date": info.get("upload_date"),
            "hashtags": info.get("tags", []),
            "engagement_rate": round(engagement_rate, 2),
            "thumbnail": info.get("thumbnail")
        }

        return metadata
    
    '''
    to dynamically extract:

    creator stats
    social metrics
    video metadata

    WITHOUT downloading video.

    Very efficient
    '''