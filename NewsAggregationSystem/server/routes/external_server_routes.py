from fastapi import APIRouter
from fastapi.params import Depends
from NewsAggregationSystem.server.controllers.external_server_controller import ExternalServerController
from NewsAggregationSystem.server.dtos.requests.external_server_update_request import ExternalServerUpdateRequest
from NewsAggregationSystem.server.middleware.check_user_role_middleware import admin_required
from fastapi import APIRouter, Body

router = APIRouter(prefix="/api/external_server")
external_server_controller = ExternalServerController()

@router.get("/")
async def get_all_servers(user_info = Depends(admin_required)):
    return external_server_controller.get_all_servers()


@router.put("/{server_id}")
async def update_server(server_id: int, external_server_data:  ExternalServerUpdateRequest = Body(...), user_info = Depends(admin_required)):
    update_data = external_server_data.dict(exclude_unset=True)
    return external_server_controller.update_server(server_id, external_server_data)

