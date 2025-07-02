from fastapi import APIRouter, Depends, Body, Query
from typing import List
from NewsAggregationSystem.server.controllers.admin_controller import AdminController
from NewsAggregationSystem.server.dtos.requests.external_server_update_request import ExternalServerUpdateRequest
from NewsAggregationSystem.server.dtos.responses.report_article_response import ReportArticleResponse
from NewsAggregationSystem.server.middleware.check_user_role_middleware import admin_required
from NewsAggregationSystem.server.dtos.requests.create_category_request import CreateCategoryRequest
from NewsAggregationSystem.server.dtos.responses.external_server_details_response import ExternalServerDetailsResponse
from NewsAggregationSystem.server.dtos.responses.update_server_details_response import UpdateServerDetailsResponse
from NewsAggregationSystem.server.dtos.responses.add_category_response import AddCategoryResponse

router = APIRouter(prefix="/api/admin", tags=["Admin"])
admin_controller = AdminController()

@router.get("/list_external_server", response_model=List[ExternalServerDetailsResponse])
async def get_all_servers(user_info=Depends(admin_required)):
    return admin_controller.get_all_servers()


@router.put("/update_external_server/{server_id}", response_model=UpdateServerDetailsResponse)
async def update_server(server_id: int, external_server_data: ExternalServerUpdateRequest = Body(...), user_info=Depends(admin_required)):
    update_data = external_server_data.dict(exclude_unset=True)
    return admin_controller.update_server(server_id, update_data)


@router.post("/add_category", response_model=AddCategoryResponse)
async def add_category(category: CreateCategoryRequest, user_info=Depends(admin_required)):
    return admin_controller.add_category(category)

@router.get("/reported-articles", response_model=List[ReportArticleResponse])
async def add_category(user_info=Depends(admin_required)):
    return admin_controller.check_reported_articles()

@router.post("/hide-reported-article/{article_id}")
def hide_reported_article(article_id :int, current_admin=Depends(admin_required)):
    return admin_controller.hide_reported_article(article_id)

@router.post("/hide-articles-by-keyword")
def hide_reported_articles_with_keyword(keyword: str = Query(...), current_admin=Depends(admin_required)):
    return admin_controller.hide_reported_articles_with_keyword(keyword)

@router.put("/hide-articles-by-category")
def hide_articles_by_category_route(category: str = Query(...), current_admin = Depends(admin_required)):
    return admin_controller.hide_articles_by_category(category)
