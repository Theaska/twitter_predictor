import uvicorn
from core.main import get_config

config = get_config()
uvicorn.run(
    'core.main:app', 
    host=config.HOST, 
    port=config.PORT, 
    log_level=config.LOG_LEVEL, 
    # reload=True
)