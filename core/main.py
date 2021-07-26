from fastapi import FastAPI
from settings import common
from core import routers


def get_config():
    return common


def get_appplication() -> FastAPI:
    config = get_config()
    
    application = FastAPI(
        title=getattr(config, "PROJECT_NAME", "FastAPI project"), 
        debug=getattr(config, "DEBUG", True),
        version=getattr(config, "VERSION", 'v1')
    )
    
    event_handlers = getattr(config, "EVENT_HANDLER", [])
    
    for event_handler in event_handlers:
        application.add_event_handler(event_handler)
        
    exception_handlers = getattr(config, "EXCEPTION_HANDLERS", [])
    
    for exception_handler in exception_handlers:
        application.add_exception_handler(exception_handler)
        
    routers_ = routers.get_routers()
    
    application.include_router(routers_, prefix=getattr(config, 'API_PREFIX'))
    
    return application

app = get_appplication()
    
    