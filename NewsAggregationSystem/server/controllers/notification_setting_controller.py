from NewsAggregationSystem.server.services.notification_setting_service import NotificationSettingService


class NotificationSettingController:
    def __init__(self):
        self.notification_setting_service = NotificationSettingService()

    def list_categories_enability(self):
        categories = self.notification_setting_service.get_all_categories_enability()
        return {"message": categories}
