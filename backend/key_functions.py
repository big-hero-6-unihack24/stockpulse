from parse_earnings_release import parse_earnings_release
import yfinance as yf
import pandas as pd
import tensorflow as tf
import numpy as np
import os

tickers = pd.read_excel('IR_website_links.xlsx', sheet_name='Sheet1')
tickers = tickers["Ticker"].to_list()

user_email = 'abc@xyz.com'
tracking_tickers = []

def get_ticker_options():
    return {'Tickers': tickers}

def add_track(ticker):
    try:
        tracking_tickers.append(ticker)
        return {'Status': 'Successfully added'}
    except Exception as e:
        return {'Status': 'Failed to add ticker'}
    
def remove_track(ticker):
    try:
        tracking_tickers.remove(ticker)
        return {'Status': 'Successfully removed'}
    except Exception as e:
        return {'Status': 'Failed to remove ticker'}


def get_stock_warning(ticker='GOOG', threshold=0.001):
    attempts = 0
    while attempts < 3:
        try:
            result = parse_earnings_release(ticker)
            break
        except Exception as e:
            attempts += 1
            if attempts == 3:
                return None


    estimates = yf.Ticker(ticker).earnings_dates
    estimates = estimates.reset_index()
    estimates = estimates.dropna()
    EPS_estimate = estimates["EPS Estimate"].to_list()[0]
    try:
        EPS_surprise =  result["EPS"]/EPS_estimate-1 
    except: 
        return None
    EPS_surprise = np.array([EPS_surprise]).reshape(-1, 1)
    model = tf.keras.models.load_model('stock_warning_model.keras')
    prediction = model.predict(EPS_surprise)[0][0]
    
    return {'Prediction': prediction,
            'Summary': result['Summary'],
            'Key': os.getenv('OPENAI_API_KEY')[-3:]}
            

