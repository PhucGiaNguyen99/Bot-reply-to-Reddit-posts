# Building bot to lead all posts with basic questions to LMGTFY

import praw
from urllib.parse import quote_plus

QUESTIONS = ["what is", "who is", "what are"]
REPLY_TEMPLATE = "[Let me google that for you](https://lmgtfy.com/?q={})"


def main():
    # Step 1: Getting started
    reddit = praw.Reddit(
        client_id="lQhGmj3cr1FYy5y9zbg5dg",
        client_secret="lp3XNcPKhlyD3N-YqaKC0oJSNezuBA",
        password="HoNgocHa12+",
        user_agent="PhucNguyen610199",
        username="PhucNguyen610199",
    )

    # Step 2: Monitoring New Submissions to r/AskReddit
    # Replace "AskReddit" with the name of another subreddit to iterate over its new submissions
    subreddit = reddit.subreddit("AskReddit")

    # Step 3: Analyzing the Submissions Titles
    # Target submissions:
    # 1. Contain no more than ten words.
    # 2. Contain one of the phrases: "what is", "what are", or "who is".
    subreddit = reddit.subreddit("AskReddit")
    for submission in subreddit.stream.submissions():
        process_submission(submission)


def process_submission(submission):
    # check if the submission's title contains any of the desired phrases:
    if len(submission.title.split()) > 10:
        return
    normalized_title = submission.title.lower()
    for question_phrase in QUESTIONS:
        if question_phrase in normalized_title:
            # Step 4: Automatically Replying to the Submission
            url_title = quote_plus(submission.title)
            reply_text = REPLY_TEMPLATE.format(url_title)
            print(f"Replying to: {submission.title}")
            submission.reply(reply_text)
            break


if __name__ == '__main__':
    main()
