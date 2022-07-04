from fastapi import APIRouter, status

router = APIRouter()

@router.get("/{trade_id}")
def get_trade(trade_id: str):
    return {"trade_id": trade_id}

@router.put("/{trade_id}")
def update_trade(trade_id: str):
    return {"trade_id": trade_id}

@router.delete("/{trade_id}")
def delete_trade(trade_id: str):
    return {"trade_id": trade_id}

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_trade():
    return {"trade_id": "123"}

@router.get("/")
def get_trades():
    return {"trades": []}