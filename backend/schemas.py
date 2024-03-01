from pydantic import BaseModel
from typing import Optional

class warning(BaseModel):
    Prediction: Optional[float]
    Summary: Optional[str]