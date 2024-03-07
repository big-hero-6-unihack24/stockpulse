from dotenv import load_dotenv
load_dotenv()

import requests
import pandas as pd
import PyPDF2
from io import BytesIO
import os
from openai import OpenAI


# use GPT-3 to extract the financial information
def parse_earnings_release(ticker):
    IR_links = pd.read_excel("IR_website_links.xlsx")
    url = IR_links[IR_links["Ticker"] == ticker]['Latest_press_release_link'].values[0]

    # extract the text from earning release
    response = requests.get(url)
    pdf_file = BytesIO(response.content)
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text_result = ""
    for page in pdf_reader.pages:
        text_result += page.extract_text()

    return extract_financials_info_from_earning_release_using_GPT(text_result)


def extract_financials_info_from_earning_release_using_GPT(text):

  client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

  instruction = "You are an assistant helping me to extract financial information from earnings releases of companies. Attachment will be provided.\
            Firstly, I will need quarterly revenue growth and earning per shares.\
            Secondly, I also need a summary of the earnings release regarding revenue, margin and guidance for revenue growth this year if any numbers are provided. \
            Provide 1 sentence summary for each factor. Total length of summary is no more than 20 words. \
            Response should be in this format: rev_grwth: x%; EPS: $y; Summary: \n First point \n Second point .... \
            All numbers should be rounded to 2 decimal places. Negative numbers should be indicated with a minus sign."

  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": instruction},
      {"role": "user", "content": text}
    ],
    temperature=0.2
  )

  response = completion.choices[0].message.content
  
  #convert the response to a dictionary
  result = {}
  for r in response.split(";"):
    key, value = r.split(":")
    key = key.strip()
    value = value.strip()
    if key == "rev_grwth":
        value = float(value.strip().replace("%", ""))/100
    elif key == "EPS" in key:
        value = float(value.strip().replace("$", ""))
    result[key] = value
    
  return result