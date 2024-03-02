import "../styles.css";
import React, { useState, useEffect  } from 'react';
import Select from 'react-select';
import axios from 'axios';

function Input() {

    const [ticker, setTicker] = useState('');
    const [tickerOptions, setTickerOptions] = useState([]);
    const [selectedTicker, setSelectedTicker] = useState(null);
    const [submitTicker, setSubmitTicker] = useState(null);

    useEffect(() => {
        fetchTickerOptions();
      });

    const fetchTickerOptions = async (ticker) => {
    try {
        let url = `${process.env.REACT_APP_BACKEND_URL}/ticker-options`;
        const response = await axios.get(url);
        let options = []; // Declare options as an empty array
        if(response.data && response.data.Tickers) {
            options = response.data.Tickers.map(ticker => ({ label: ticker, value: ticker }));
            console.log('options: ', options);
        }
        setTickerOptions(options);
        console.log('tickerOptions: ', tickerOptions);
        return options;
    } catch (error) {
        console.error('Error fetching tickers: ', error);
    }
    };

    const handleTickerChange = (newValue) => {
        setTicker(newValue);
        return newValue;
    };

    const handleChange = (selectedTicker) => {
        setTicker(selectedTicker);
    }

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
          setSubmitTicker(selectedTicker);
        //   const response = await axios.post();
        } catch (error) {
          console.error('Error fetching data: ', error);
        }
    };

    return (
        <div className="input-bar">
            {/* <span><input className="ticker" type="text" placeh</form>older="Select stock to track..."></input></span> */}
            <form onSubmit={handleSubmit}>
                <Select
                    className='ticker'
                    name="ticker"
                    inputValue={ticker}
                    onInputChange={handleTickerChange}
                    onChange={handleChange}
                    options={tickerOptions}
                    placeholder="Select stock to track..."
                />
                <input 
                    className="threshold" 
                    type="number" 
                    step="0.01" 
                    placeholder="Set threshold (in %).."
                />
                <button type="submit" class="button">Submit</button>
            </form>
                
            {/* </span> */}
            {/* <span><input className="threshold" type="text" placeholder="What is your threshold?..."></input></span> */}
            {/* <span><button>Submit</button></span> */}


        </div>
    )
}

export default Input;