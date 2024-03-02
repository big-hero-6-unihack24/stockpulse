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
    EPS_surprise = np.array([EPS_surprise]).reshape(-1, 1)
    model = tf.keras.models.load_model('stock_warning_model.keras')
    prediction = model.predict(EPS_surprise)[0][0]
    if prediction > threshold:
        email_warning(ticker, prediction, result['Summary'], company_name)
    
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

    html_content = """
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Anybody:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #dfe5e5;
            }}
            #background-container {{
                background-color: #dfe5e5;
                padding-top: 2%;
                padding-bottom: 2%;
            }}
            .container {{
                width: 80%;
                margin: 0 auto;
                border-radius: 5px;
                background-color: #ffffff;
                box-shadow: 0px 1px 0px #111f1f;
                max-width: 1000px;
                min-width: 900px;
            }}
            .flex {{
                display: flex;
                text-align: center;
                justify-content: center;
                width: 100%;
                padding: 2% 30% 2%;
                padding-left: 20
            }}
            #stock-name {{
                font-size: 2em;
                font-weight: bold;
                text-transform: uppercase;
                text-align: center;
            }}
            #potential-forecast{{
                padding: 2%;
                text-align: center;
                font-family: 'Anybody', Arial, sans-serif;
                font-weight: bold;
                margin-bottom: 2%;
            }}
            #forecast-container {{
                margin-top: 2%;
            }}

            #stock-alert-title{{
                font-size: 2em;
                font-weight: 600;
                text-align: center;
                margin-bottom: 5%;
                margin-top: 5%;
                background-color: #4A4A48;
                padding: 5% 0% 5%;
                color: #ffffff;
                border-top-left-radius: 5px;
                border-top-right-radius: 5px;
                font-family: 'Anybody', Arial, sans-serif;
            }}
            #percent-change {{
                font-size: 1.5em;
                text-align: center;
                font-family: 'Anybody', Arial, sans-serif;
            }}
            #summary-title {{
                font-size: 1.5em;
                text-align: center;
                padding: 3%;
                font-family: 'Anybody', Arial, sans-serif;
            }}
            #summary-container {{
                background-color: #F0C808;
                border-radius: 5px;
            }}
            #content-container{{
                padding: 0% 2% 2%;
            }}
            #content-container{{
                padding: 0% 3% 2%;
            }}
            #summary-content {{
                text-align: center;
                padding-left: 2%;
                padding-right: 2%;
                padding-bottom: 2%;
            }}
            #urgent-action {{
                text-align: center;
                font-size: 2.0em;
                font-weight: bolder;
                font-family: 'Anybody', Arial, sans-serif;
                color: #DD1C1A;
            }}
            #stock-container{{
                /* margin-right: 5%; */
                padding: 5%;
            }}
            #company-name{{
                font-size: 0.8em;
                text-align: center;
                color: #808080;
            }}
            #introduction {{
                text-align: center;
            }}
            #closing-container {{
                padding-left: 2%;
                margin-top: 5%
            }}
            #date-container{{
                text-align: center;
                font-weight: bold;
                margin-bottom: 2%;
            }}
            p {{
                font-size: 1.1em;
            }}
        </style>
    </head>
    <body>
        <div id="background-container">
            <div class="container">
                <div id="stock-alert-title">
                    Stock Alert by StockPulse
                </div>
                <div id="content-container">
                    <div id="urgent-action">
                        Urgent Action Needed !
                    </div>
                    <p id="introduction">A drastic change in stock has been detected. The stock in question can be seen below.</p>
                    <div class="flex">
                        <div id="stock-container">
                            <div id="stock-name">
                                {}
                            </div>
                            <div id="company-name">
                                {}
                            </div>
                        </div>
                        <div id="forecast-container">
                            <div id="potential-forecast">
                                Potential Forecasted Change
                            </div>
                            <div id="percent-change">
                                {}
                            </div>
                        </div>
                    </div>
                    <div id="date-container">
                        {}
                    </div>
                    <div id="summary-container">
                        <div id="summary-title">
                            Summary of Earnings
                        </div>
                        <div id="summary-content">
                            {}
                        </div>
                    </div>
                    
                    <div id="closing-container">
                        <p>Please look at your earnings. We hope this information was useful.</p>
                        <p>All the best,<br> StockPulse Team</p>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """.format(stock_name, company_name, percent_change, latest_warning, summary)

    em.add_alternative(html_content, subtype='html')

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender_email, password)
        smtp.sendmail(sender_email, user_email, em.as_string())
