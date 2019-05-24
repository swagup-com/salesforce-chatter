#!/usr/bin/env python
import os

from ..chatter import Chatter, ChatterAuth

USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')


def post_text_with_mention(subject_id="0017A00000TW5tbQAD", text="Mockups generated successfully!!!",
                           mention_to="0057A0000024xF7QAI"):
    auth = ChatterAuth(username=USERNAME, password=PASSWORD, client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

    chatter = Chatter(auth=auth)

    feed_item = {
        "body": {
            "messageSegments": [
                {
                    "type": "Text",
                    "text": text
                },
                {
                    "type": "Mention",
                    "id": mention_to
                }
            ]
        },
        "feedElementType": "FeedItem",
        "subjectId": subject_id
    }
    return chatter.feed_elements(feed_item)


def main():
    print(post_text_with_mention())


if __name__ == '__main__':
    main()
