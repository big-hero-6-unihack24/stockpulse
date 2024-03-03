import "../styles.css";
import React, { useState, useEffect } from 'react';
import Select from 'react-select';
import axios from 'axios';

function Input({ addSelectedTicker }) {
    const [tickerOptions, setTickerOptions] = useState([]);
    const [selectedTicker, setSelectedTicker] = useState(null);

    useEffect(() => {
        const fetchTickerOptions = async () => {
            try {
                const url = `${process.env.REACT_APP_BACKEND_URL}/ticker-options`;
                const response = await axios.get(url);
                console.log('Fetched ticker options:', response.data);
                const options = response.data.Tickers.map(ticker => ({ label: ticker, value: ticker }));
                setTickerOptions(options);
            } catch (error) {
                console.error('Error fetching tickers:', error);
            }
        };

        fetchTickerOptions();
    }, []);

    const handleChange = (selectedOption) => {
        setSelectedTicker(selectedOption);
        
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (selectedTicker) {
            addSelectedTicker(selectedTicker);
            setSelectedTicker(null);
        }
        console.log('Submitting ticker:', selectedTicker);
    
    };

    const customSelectStyles = {
        control: (provided) => ({
            ...provided,
            borderRadius: '10px 0 0 10px',
            padding: '12px 32px',
            border: '0',
            boxShadow: 'none',
            outline: '0',
            
        }),
    };

    return (
        <div class="input-section">
            <form className="input-bar" onSubmit={handleSubmit}>
                <span className="select-container">
                    <Select
                        className='ticker'
                        name="ticker"
                        value={selectedTicker}
                        options={tickerOptions}
                        onChange={handleChange}
                        placeholder="Select stock to track..."
                        styles={customSelectStyles}
                    />
                </span>
                <span>
                    <input 
                        className="threshold" 
                        type="number" 
                        step="0.01" 
                        placeholder="Set threshold (in %).." 
                    />
                </span>
                <span>
                    <button type="submit" className="button" >Submit</button>
                </span>
            </form>
        </div>
    );
}

export default Input;
