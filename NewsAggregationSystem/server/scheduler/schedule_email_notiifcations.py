from apscheduler.schedulers.asyncio import AsyncIOScheduler
from NewsAggregationSystem.server.services.notification_service import NotificationService
from NewsAggregationSystem.server.utilities.logger import logger
import time

notification_service = NotificationService()

async def run_send_notifications_job():
    start_time = time.time()
    await notification_service.send_notifications_by_email()
    elapsed = time.time() - start_time
    logger.info(f"Time taken to send email notifications to all users: {elapsed:.2f} seconds")

def start_scheduler_for_email_notification():
    scheduler = AsyncIOScheduler()

    scheduler.add_job(
        run_send_notifications_job,
        trigger='interval',
        hours = 1
    )

    scheduler.start()
