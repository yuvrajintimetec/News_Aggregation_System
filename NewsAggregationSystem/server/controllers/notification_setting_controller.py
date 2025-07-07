from NewsAggregationSystem.server.services.notification_setting_service import NotificationSettingService
from fastapi import HTTPException, status
from NewsAggregationSystem.server.exceptions.not_found_exception import NotFoundException


class NotificationSettingController:
    def __init__(self):
        self.notification_setting_service = NotificationSettingService()

    def list_categories_enability(self):
        try:
            categories = self.notification_setting_service.get_all_categories_enability()
            return {"message": categories}
        except NotFoundException as error:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error))
