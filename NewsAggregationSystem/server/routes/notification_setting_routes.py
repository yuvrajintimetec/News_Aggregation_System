from fastapi import APIRouter, Depends
from NewsAggregationSystem.server.controllers.notification_setting_controller import NotificationSettingController
from NewsAggregationSystem.server.dtos.responses.category_config_response import CategoryConfigResponse
from NewsAggregationSystem.server.middleware.authentication_middleware import get_current_user

router = APIRouter(prefix="/api/notification-setting")
notification_setting_controller = NotificationSettingController()

@router.get("/category-enability", response_model=CategoryConfigResponse)
def list_categories_enability(user_info=Depends(get_current_user)):
    return notification_setting_controller.list_categories_enability()
