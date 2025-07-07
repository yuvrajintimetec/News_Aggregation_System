import requests
import os
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler
from NewsAggregationSystem.server.utilities.logger import logger
import time

load_dotenv()

def call_fetch_articles_api():
    start_time = time.time()
    try:
        base_url = os.getenv("BASE_URL")
        response = requests.get(f"{base_url}/articles/external_source")
        logger.info(f"Scheduler Response: {response.status_code}")
    except requests.exceptions.ConnectionError:
        return {"error": "Server is not reachable."}
    except Exception as e:
        logger.error(f"Error: {str(e)}")
    finally:
        elapsed = time.time() - start_time
        logger.info(f"Time taken to fetch articles: {elapsed:.2f} seconds")

def start_scheduler_for_fetching_articles():
    scheduler = BackgroundScheduler()
    scheduler.add_job(call_fetch_articles_api, 'interval', hours=3)
    scheduler.start()
