# -*- coding: utf-8 -*-

# Sample Python code for youtube.liveBroadcasts.update
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

# pip install --upgrade google-api-python-client
# pip install --upgrade google-auth-oauthlib google-auth-httplib2

import os
from time import sleep

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube",
          "https://www.googleapis.com/auth/youtube.force-ssl"]

# Disable OAuthlib's HTTPS verification when running locally.
# *DO NOT* leave this option enabled in production.
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"

api_service_name = "youtube"
api_version = "v3"
client_secrets_file = "ytcred.json"

# Get credentials and create an API client
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    client_secrets_file, scopes)
credentials = flow.run_console()
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, credentials=credentials)


max_viewers = 0


def getVideoInfo(vidID):
    request = youtube.videos().list(  # pylint: disable = maybe-no-member
        part="snippet,liveStreamingDetails",
        id=vidID)
    response = request.execute()
    items = response['items']
    concurrentViewers = items[0]['liveStreamingDetails']['concurrentViewers']
    liveordead = items[0]['snippet']['liveBroadcastContent']

    return concurrentViewers, liveordead



def main():
    videoID = input('Enter video ID: ')

    
    while True:
        conViewers, alive = getVideoInfo(videoID)
        if alive == 'none':
            break

        if conViewers != 'undefined':
            if int(conViewers) > max_viewers:
                max_viewers = int(conViewers)
                
            request = youtube.liveBroadcasts().update(  # pylint: disable = maybe-no-member
            part="snippet",
            body={
                "id": videoID,
                "snippet": {
                    "title": f"Wow! I cannot believe {conViewers:,} people are watching me sit in front of my computer."
                    }
                }
            )
        
            request.execute()

        sleep(5)

    
    request = youtube.videos().update(  # pylint: disable = maybe-no-member
            part="snippet",
            body={
                "id": videoID,
                "snippet": {
                    "title": f"Can you believe {max_viewers:,} people watched me sit in front of my computer."
                    }
                }
            )
        
    request.execute()


if __name__ == "__main__":
    main()


# TODO: quit on key command or stop button
# TODO: GUI to insert video ID, title
