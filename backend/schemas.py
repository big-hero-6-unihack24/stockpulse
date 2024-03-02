from pydantic import BaseModel
from typing import Optional, List

class warning(BaseModel):
    Ticker: Optional[str]
    Company: Optional[str]
    Prediction: Optional[float]
    Summary: Optional[str]
    Key: Optional[str]

class TickerOptions(BaseModel):
    Tickers: List[str]

class newtrackresponse(BaseModel):
    Status: str

class tracking_tickers(BaseModel):
    Tickers: List[str]

class removetrackresponse(BaseModel):
    Status: str

class get_email_response(BaseModel):
    Email: str

class debug(BaseModel):
    tracking_tickers: List[Optional[str]]
    user_email: str
    allowed_origins: List[str]
    allowed_hosts: List[str]
    containter_tag: str