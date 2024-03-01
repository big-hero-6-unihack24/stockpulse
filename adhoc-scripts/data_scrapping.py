import yfinance as yf
import pandas as pd

def get_earnings_data(ticker):
    stock = yf.Ticker(ticker)
    data = stock.earnings_dates
    data = data.reset_index()
    data = data.dropna()
    data['Earnings Date'] = data['Earnings Date'].dt.strftime('%Y-%m-%d')
    data['Earnings Date'] = pd.to_datetime(data['Earnings Date'])

    # create a new column and add one date to earnings date
    data['date_after_earnings'] = data['Earnings Date'] + pd.DateOffset(1)
    data['date_before_earnings'] = data['Earnings Date'] + pd.DateOffset(-1)
    data = data.sort_values(by='date_before_earnings', ascending=True)

    hist_price = stock.history(period="5y")
    hist_price = hist_price.reset_index()
    hist_price = hist_price.dropna()
    hist_price['Date'] = hist_price['Date'].dt.strftime('%Y-%m-%d')
    hist_price['Date'] = pd.to_datetime(hist_price['Date'])
    hist_price = hist_price.sort_values(by='Date', ascending=True)

    merged_data = pd.merge_asof(data, hist_price, left_on='date_before_earnings', right_on='Date', direction='backward')
    merged_data = merged_data[['Earnings Date', 'EPS Estimate', 'Reported EPS', 'Surprise(%)', 'date_after_earnings', 'Date', 'Close']]
    merged_data = merged_data.rename(columns={'Close': 'Close_before_earnings', 'Date': 'date_before_earnings'})
    merged_data = pd.merge_asof(merged_data, hist_price, left_on='date_after_earnings', right_on='Date', direction='forward')
    merged_data = merged_data[['Earnings Date', 'EPS Estimate', 'Reported EPS', 'Surprise(%)', 'date_before_earnings', 'Close_before_earnings', 'Date', 'Close']]
    merged_data = merged_data.rename(columns={'Close': 'Close_after_earnings', 'Date': 'date_after_earnings'})
    merged_data = merged_data.dropna()
    merged_data['Share Price Change'] = merged_data['Close_after_earnings'] / merged_data['Close_before_earnings'] -1
    merged_data = merged_data[['Earnings Date', 'Surprise(%)', 'Share Price Change']]
    merged_data = merged_data.rename(columns={'Surprise(%)': 'Surprise'})
    
    return merged_data

if __name__ == "__main__":
    tickers = pd.read_excel('Tickers.xlsx', engine='openpyxl')
    tickers = tickers['Symbol'].tolist()

    # create an empty dataframe and append the data to it
    earnings_data = pd.DataFrame()
    for ticker in tickers:
        try:
            data = get_earnings_data(ticker)
            earnings_data = pd.concat([earnings_data, data], ignore_index=True)
            print(f"Data for {ticker} has been added to the dataframe")
        except:
            print(f"Error with {ticker}")
            continue

    earnings_data.to_csv('earnings_data.csv', index=False)

