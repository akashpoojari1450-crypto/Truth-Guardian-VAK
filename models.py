from pydantic import BaseModel
from typing import Optional, Dict

class NewsObservation(BaseModel):
    echoed_message: str
    message_length: int
    done: bool
    reward: Optional[float] = None
    metadata: Dict = {}

class DetectionAction(BaseModel):
    message: str
    label: Optional[str] = None # Added label for the Environment class
