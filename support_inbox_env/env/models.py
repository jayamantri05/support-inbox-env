from pydantic import BaseModel
from typing import Optional, List

class Observation(BaseModel):
    ticket_id: str
    customer_message: str
    history: List[str]
    status: str

class Action(BaseModel):
    action_type: str
    message: Optional[str] = None
    refund_amount: Optional[float] = None

class Reward(BaseModel):
    score: float
    reason: str