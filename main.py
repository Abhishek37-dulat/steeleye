from fastapi import FastAPI

from service.trade_service import router as trade_router

app = FastAPI()

app.include_router(trade_router, prefix="/trades", tags=["trades"])

@app.get("/")
def read_root():
    return "welcome to steeleye's trade api"
