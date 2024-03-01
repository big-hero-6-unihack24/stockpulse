from pydantic import BaseModel
from typing import Optional, List

class warning(BaseModel):
    Prediction: Optional[float]
    Summary: Optional[str]

class TickerOptions(BaseModel):
    Tickers: List[str]