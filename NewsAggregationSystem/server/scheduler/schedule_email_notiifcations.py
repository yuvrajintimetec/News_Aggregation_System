from apscheduler.schedulers.asyncio import AsyncIOScheduler
from NewsAggregationSystem.server.services.notification_service import NotificationService

notification_service = NotificationService()

async def run_send_notifications_job():
    await notification_service.send_notifications_by_email()

def start_scheduler_for_email_notification():
    scheduler = AsyncIOScheduler()

    scheduler.add_job(
        run_send_notifications_job,
        trigger='interval',
        hours=2
    )

    scheduler.start()
