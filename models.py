from pydantic import BaseModel

class NewsObservation(BaseModel):
    news_text: str

class DetectionAction(BaseModel):
    label: str
