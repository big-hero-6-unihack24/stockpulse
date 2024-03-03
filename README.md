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

# How We Built It
Our project seamlessly integrates frontend and backend components, leveraging a variety of scripts, packages, and APIs to deliver a comprehensive solution. Here's a breakdown of the technologies and methodologies we employed:

## Frontend
The user interface of our application is powered by the ReactJS framework, utilizing HTML and CSS for structuring and styling, respectively. JavaScript plays a crucial role in dynamically managing frontend components and facilitating interaction with the backend. To ensure a smooth and continuous deployment process, we hosted the frontend on GitHub Pages and utilized GitHub Actions for CI/CD, enabling automatic updates and deployments.


## Backend

### Server
Our backend infrastructure is built on the FastAPI framework, known for its high performance, and is served via a Uvicorn ASGI server. This combination offers a robust and scalable solution for our application's needs.

### Web-scraping
To gather the latest earnings and financial releases, we employed BeautifulSoup and PyPDF2 for scraping data from companies' investor relations websites, converting it into a text format for further processing. Additionally, historical financial data is sourced from Yahoo Finance using the yfinance library. Given Yahoo Finance's update latency of 2-3 days post-release, our direct scraping from investor relations sites ensures timely data retrieval, critical for our analysis.


### Process the information
We utilize OpenAI's GPT-3.5-turbo model to distill key financial insights from the scraped text data, providing succinct summaries of earnings releases. This processed information, combined with data from Yahoo Finance, feeds into our predictive model to assess potential significant stock price movements following an earnings announcement.

### AI model
At the heart of our predictive capability is a custom-built neural network model, developed using TensorFlow. This model analyzes the amalgamated data to forecast potential shifts in stock prices, offering our users valuable insights to inform their investment decisions.


# Challenges We Encountered
One of the primary challenges we faced was sourcing the financial data necessary to train our model. Accessing comprehensive and accurate data often required premium API subscriptions, which posed a significant obstacle. Additionally, constructing a meaningful AI model within a constrained timeframe proved to be a daunting task. These challenges tested our resolve and pushed us to think creatively in our approach.

# Future Directions for StockPulse
As we look to the horizon, we have identified several key enhancements to elevate StockPulse's capabilities:

- Enriching AI Analysis: Integrating additional factors into our AI's analytical framework to provide deeper insights.
- Model Optimization: Refining our AI model to achieve greater accuracy and reliability in its predictions.
- Comprehensive Monitoring: Extending our platform's capabilities to include alerts on news and events related to tracked companies, offering a more holistic view of potential impacts.
- Market Trend Detection: Analyzing real-time stock prices to identify emerging market trends, enabling users to make more informed decisions.
- Dashboard Implementation: Developing a user-friendly dashboard to offer users a comprehensive overview of their portfolio and individual stock performance.

# Our Proud Achievements
Embarking on the StockPulse project was a journey of many firsts for us. It marked our inaugural venture into developing a live project as a team within a limited timeframe. For all of us, this was the first hackathon experience, introducing us to the exhilarating process of transforming an idea into reality alongside a newly formed team. This experience was a crucible of learning, from mastering project management skills to rapidly acquiring and applying new coding techniques. We take pride in not just the technical skills we've honed but also in the invaluable lessons learned in teamwork, perseverance, and innovation.