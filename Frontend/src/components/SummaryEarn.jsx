import React, { useState, useEffect } from 'react';
import "../styles.css";
import axios from 'axios';

const SummaryEarn = () => {
    const [warning, setWarning] = useState(null);
    // const [ticker, setTicker] = useState('');
    // const [threshold, setThreshold] = useState('');

    let ticker = 'GOOG';
    let threshold = 0.001;

    useEffect(() => {
        fetchWarning(ticker, threshold);
    });

    const fetchWarning = async (ticker, threshold) => {
        try {
            let url = `${process.env.REACT_APP_BACKEND_URL}/warning?ticker=${ticker}&threshold=${threshold}`;
            const response = await axios.get(url);
            setWarning(response.data);
            console.log('response: ', response.data);
            console.log('warning: ', warning);
            return response.data;
        } catch (error) {
            console.error('Error fetching warning: ', error);
        }
    }
    

    return (
        <div class="warning">
            <h2>Latest warning</h2>
            {warning && (
                <div>
                    <h3>{ticker}</h3>
                    <p>Prediction: {warning.Prediction ? `${(warning.Prediction * 100).toFixed(1)}%` : '-'}</p>
                    <p>{warning.Summary}</p>
                </div>
            )}
        </div>
    )
}

export default SummaryEarn;