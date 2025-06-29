from fastapi import FastAPI
from NewsAggregationSystem.server.routes import authentication_routes, article_routes, external_server_routes, category_routes, user_routes, admin_routes
from NewsAggregationSystem.server.scheduler.schedule_fetch_articles import start_scheduler_for_fetching_articles
from NewsAggregationSystem.server.scheduler.schedule_email_notiifcations import start_scheduler_for_email_notification

app = FastAPI()

app.include_router(authentication_routes.router)
app.include_router(article_routes.router)
app.include_router(external_server_routes.router)
app.include_router(user_routes.router)
app.include_router(admin_routes.router)

start_scheduler_for_fetching_articles()

@app.on_event("startup")
async def startup_event():
    start_scheduler_for_email_notification()