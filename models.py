from pydantic import BaseModel
from typing import Optional, Dict

class NewsObservation(BaseModel):
    echoed_message: str
    message_length: int
    done: bool = False
    reward: Optional[float] = None
    metadata: Dict = {}

class DetectionAction(BaseModel):
    message: str
    label: Optional[str] = "FAKE"
