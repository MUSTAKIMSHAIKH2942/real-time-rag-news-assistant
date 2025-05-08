
import schedule
import time
from data_pipeline.fetch_news import fetch_news

def job():
    print("Fetching news...")
    fetch_news()

schedule.every(30).minutes.do(job)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)
