from parse_earnings_release import parse_earnings_release
import yfinance as yf
import pandas as pd
import tensorflow as tf
import numpy as np

def get_stock_warning(ticker='GOOG', threshold=0.001):
    result = parse_earnings_release(ticker)
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
    
    if prediction < threshold:
        return {'Prediction': None,
            'Summary': None}

    return {'Prediction': prediction,
            'Summary': result['Summary']}