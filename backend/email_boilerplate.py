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
                    <p id="introduction">Our AI detected a potential drastic price change. The stock in question can be seen below.</p>
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
                                {}%
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
                        <p>Please look at the earnings release. We hope this information was useful.</p>
                        <p>All the best,<br> StockPulse Team</p>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """