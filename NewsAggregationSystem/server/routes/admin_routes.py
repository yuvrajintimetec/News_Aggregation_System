from fastapi import APIRouter, Depends, Body
from NewsAggregationSystem.server.controllers.admin_controller import AdminController
from NewsAggregationSystem.server.dtos.requests.external_server_update_request import ExternalServerUpdateRequest
from NewsAggregationSystem.server.middleware.check_user_role_middleware import admin_required
from NewsAggregationSystem.server.dtos.requests.create_category_request import CreateCategoryRequest

router = APIRouter(prefix="/api/admin", tags=["Admin"])
admin_controller = AdminController()

@router.get("/list_external_server")
async def get_all_servers(user_info=Depends(admin_required)):
    return admin_controller.get_all_servers()


@router.put("/update_external_server/{server_id}")
async def update_server(server_id: int, external_server_data: ExternalServerUpdateRequest = Body(...), user_info=Depends(admin_required)):
    update_data = external_server_data.dict(exclude_unset=True)
    admin_controller.update_server(server_id, update_data)
    return {"message": "server details updated successfully"}

@router.post("/add_category")
async def add_category(category: CreateCategoryRequest, user_info=Depends(admin_required)):

    if admin_controller.add_category(category):
        return {"messsage": "category added successfully"}
    else:
        return {"error": "category already exists"}