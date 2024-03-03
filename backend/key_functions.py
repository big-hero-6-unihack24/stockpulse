from dotenv import load_dotenv
load_dotenv()

from parse_earnings_release import parse_earnings_release
import yfinance as yf
import pandas as pd
import tensorflow as tf
import numpy as np
import os
from email.message import EmailMessage
import smtplib
import ssl
import datetime
from email_boilerplate import html_content

tickers = pd.read_excel('IR_website_links.xlsx', sheet_name='Sheet1')
ticker_list = tickers["Ticker"].to_list()

user_email = 'abc@xyz.com'
tracking_tickers = []

def get_ticker_options():
    return {'Tickers': ticker_list}

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
    x_factor = np.random.uniform(0.1, 0.2) if EPS_surprise > 0 else -np.random.uniform(0.1, 0.2)
    EPS_surprise = np.array([EPS_surprise]).reshape(-1, 1) #temp fix before we improve the AI model with more inputs and training data
    model = tf.keras.models.load_model('stock_warning_model.keras')
    prediction = model.predict(EPS_surprise)[0][0] + x_factor

    if prediction > threshold:
        email_warning(ticker, prediction, result['Summary'], tickers[tickers['Ticker'] == ticker]['Company'].values[0])
    
    return {'Ticker': ticker,
            'Company': tickers[tickers['Ticker'] == ticker]['Company'].values[0],
            'Prediction': prediction,
            'Summary': result['Summary'],
            'Key': os.getenv('OPENAI_API_KEY')[-3:]}
            


def email_warning(ticker, prediction, summary, company_name):
    sender_email = "coding.test.projects@gmail.com"
    subject = "STOCK ALERT. DRASTIC CHANGE"
    message = """STOCK ALERT. DRASTIC CHANGE"""

    em = EmailMessage()
    em['From'] = sender_email
    em['To'] = user_email
    em['subject'] = subject
    em.set_content(message)

    stock_name = ticker
    percent_change = round(prediction * 100, 2)
    percent_change = str(percent_change) + "%"

    current_datetime = datetime.datetime.now()
    latest_warning = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    percent_change = round(prediction * 100, 2)

    email_content = html_content.format(stock_name, company_name, percent_change, latest_warning, summary)

    em.add_alternative(email_content, subtype='html')

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender_email, os.getenv('email_password'))
        smtp.sendmail(sender_email, user_email, em.as_string())