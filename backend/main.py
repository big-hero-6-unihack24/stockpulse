from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from pydantic import BaseModel
import key_functions
import schemas
from config import cors_allowed_origins_list

# Create a FastAPI app
app = FastAPI()

app.add_middleware(
     TrustedHostMiddleware, 
     allowed_hosts=["localhost", "127.0.0.1"]
) #add backend host when deployed to Azure

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_allowed_origins_list, #add frontend allowed origins when deployed to Azure
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def read_root():
    return {'Hello': 'World'}

@app.get('/warning', response_model=schemas.warning)
def warning(ticker: str, threshold: float = 0.001):
    return key_functions.get_stock_warning(ticker, threshold)
