from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from pydantic import BaseModel
import key_functions
import schemas
from config import cors_allowed_origins_list, cors_allowed_hosts_list
from typing import List
import os

# Create a FastAPI app
app = FastAPI()

# app.add_middleware(
#      TrustedHostMiddleware, 
#      allowed_hosts=cors_allowed_hosts_list
# ) #add backend host when deployed to Azure

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
    response = key_functions.get_stock_warning(ticker, threshold)
    return response
    
@app.get('/ticker-options', response_model=schemas.TickerOptions)
async def get_ticker_options():
    return key_functions.get_ticker_options()

@app.post('/newtrack', response_model=schemas.newtrackresponse)
async def add_track(ticker: str):
    response = key_functions.add_track(ticker)
    return response

@app.get('/tracking-tickers', response_model=schemas.tracking_tickers)
async def get_tracking_tickers():
    return {'Tickers': key_functions.tracking_tickers}

@app.post('/removetrack', response_model=schemas.removetrackresponse)
async def remove_track(ticker: str):
    response = key_functions.remove_track(ticker)
    return response

@app.post('/update-email', response_model=schemas.newtrackresponse)
async def update_email(email: str):
    key_functions.user_email = email
    return {'Status': 'Email updated'}

@app.get('/get-email', response_model=schemas.get_email_response)
async def get_email():
    return {'Email': key_functions.user_email}

@app.get('/debug', response_model=schemas.debug)
async def debug():
    return {'tracking_tickers': key_functions.tracking_tickers, 
            'user_email': key_functions.user_email,
            'allowed_origins': cors_allowed_origins_list,
            'allowed_hosts': cors_allowed_hosts_list,
            'containter_tag': 'v7'}




