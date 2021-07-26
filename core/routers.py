from fastapi import APIRouter


def get_routers():
    router = APIRouter()
    # router.include_router(app_name.routers.routers, tags=['tags'], prefix=app_name.routers.prefix)
    return router