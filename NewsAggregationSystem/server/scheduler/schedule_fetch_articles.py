import requests
import os
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler

load_dotenv()

def call_fetch_articles_api():
    try:
        base_url = os.getenv("BASE_URL")
        response = requests.get(f"{base_url}/articles/external_source")
        print("Scheduler Response:", response.status_code)
    except Exception as e:
        print("Error:", str(e))

def start_scheduler_for_fetching_articles():
    scheduler = BackgroundScheduler()
    scheduler.add_job(call_fetch_articles_api, 'interval', hours=3)
    scheduler.start()
