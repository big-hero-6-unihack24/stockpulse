# StockPulse
Revolutionize your investments with real-time, data-driven insights and alerts tailored to stock movements post-earnings, designed to keep you one step ahead in the market.

# Inspiration
Are you a fundamental stock investor?

In the fast-paced world of stock investing, staying updated with the latest financial performances of companies is crucial. As fundamental stock investors ourselves, we understand the challenges many people are facing - keeping track of earnings releases amidst a busy life of work, study, or travel can be daunting. Missing out on these critical updates can sometimes lead to significant losses, especially when markets react before you get the chance to. That's where the idea for StockPulse was born.

# What it does
## Description of the product
StockPulse is your vigilant financial assistant, designed to monitor earnings announcements from companies you're invested in. Upon detecting a new earnings release, StockPulse swiftly retrieves the report directly from the company's website, analyzes it, and sends you an alert about potential significant stock movements. This real-time information empowers you to make informed decisions swiftly.

## Target audience
StockPulse is crafted for retail investors who aren't working full-time in investment funds but are passionate about managing their investments wisely. Whether you're a seasoned investor or just starting, StockPulse offers you the insights you need without overwhelming you with information.

## What problem does it solve
The core mission of StockPulse is to streamline your investment strategy by:
- Keeping you informed of crucial financial events without cluttering your inbox with spam.
- Saving you time by automating the tracking of earnings releases and financial performance of your investments.
- Empowering your investment decisions, allowing you to focus on what matters most in your life while securing your financial future.

## What makes this product unique
- Real-Time Alerts: Instant notifications about earnings releases, so you're always in the know.
- AI-Driven Insights: Sophisticated analysis of earnings reports to highlight potential market movements.
- User-Centric Design: Tailored for retail investors seeking a balance between their investment portfolio and busy lifestyle.

# How to run
## Backend
Download dependencies for python environment
```
pip install -r .\backend\requirements.txt
```
Start FastAPI server. Upon startup, the server is accessible at localhost:8000
```
cd backend
uvicorn main:app --reload
```

## Frontend
Download dependencies for NodeJS
```
cd frontend
npm install
```
Set up environment variable to connect with backend
```
echo REACT_APP_BACKEND_URL=localhost:8000 >> .env
```
Start frontend server. Upon startup, the server is accessible at localhost:3000
```
npm start
```

# How we built it
Our project contains both frontend and backend components. The scripts, packages, and APIs we used in this project are as follows:

## Frontend
Our frontend is built on ReactJS framework. HTML and CSS are used to define the structure and aesthetic of the web app. JavaScript is used to dynamically control components of frontend and interact with backend. 
For live site, we hosted the frontend on Github Pages and deployed it using Github Actions for continuous integration/continuous deployment.

## Backend
Our backend is built using FastAPI run on Uvicorn server. The following tech stack are used in our backend.
## Web-scraping
BeautifulSoup and PyPDF libraries are used to scrape and extract latest earnings/financials release on companies' investors relation websites to text format.
In addition, we extract history financial data of the tracked company from Yahoo Finance using yfinance libary. Yahoo Finance normally takes 2-3 days to update with new fiancial releases, so data scrapped from investors relation websites will not exist on Yahoo Finance at the moment StockPulse perform analysis.
## Process the information
We then leverage OpenAI's gpt-3.5-turbo model to extract the key financial information from text data scrapped and provide a quick summary release.
After that, the combined data from Yahoo Finance and company's website is fed into our AI model to predict if there is potential big move in share price a day after earning release.
## AI model
We built a neural network model, using Tensorflow, to process data and provide a prediction.