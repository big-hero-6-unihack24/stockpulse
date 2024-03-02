import React, { useState, useEffect } from 'react';
import "../styles.css";
import axios from 'axios';

const LatestWarn = () => {
    const [warning, setWarning] = useState(null);
    // const [ticker, setTicker] = useState('');
    // const [threshold, setThreshold] = useState('');

    const [warningDate, setWarningDate] = useState('');

    let ticker = 'GOOG';
    let threshold = 0.001;


useEffect(() => {
    const fetchWarning = async (ticker, threshold) => {
        try {
            let url = `${process.env.REACT_APP_BACKEND_URL}/warning?ticker=${ticker}&threshold=${threshold}`;
            const response = await axios.get(url);
            if (response.data) {
                setWarning(response.data);
                setWarningDate(new Date().toLocaleDateString());
            }
          
            // console.log('response: ', response.data);
            // console.log('warning: ', warning);
            // return response.data;
        } catch (error) {
            console.error('Error fetching warning: ', error);
        }
    };
    fetchWarning();

}, [ticker, threshold]);
    
    

    return (
        <div class="warning">
        <div className='warning-day'>
            <div><h2>Latest warning</h2></div>
            <div><p>{warningDate}</p></div>
        </div>
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

export default LatestWarn;
