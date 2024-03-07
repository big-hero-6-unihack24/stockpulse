import React, { useState, useEffect } from 'react';
import "../styles.css";
import axios from 'axios';
import { AiOutlineArrowUp, AiOutlineArrowDown } from "react-icons/ai";

const LatestWarn = ({ selectedTickers }) => {
    const [warnings, setWarnings] = useState({});
    const [warningDates, setWarningDates] = useState({});

    const threshold = 0.001;

    useEffect(() => {
        selectedTickers.forEach(ticker => {
            const fetchWarning = async () => {
                try {
                    const url = `${process.env.REACT_APP_BACKEND_URL}/warning?ticker=${ticker.value}&threshold=${threshold}`;
                    const response = await axios.get(url);
                    if (response.data) {
                        setWarnings(prevWarnings => ({ ...prevWarnings, [ticker.value]: response.data }));
                        setWarningDates(prevDates => ({ ...prevDates, [ticker.value]: new Date().toLocaleDateString() }));
                    }
                } catch (error) {
                    console.error('Error fetching warning: ', error);
                }
            };
            fetchWarning();
        });
    }, [selectedTickers]);

    return (
    
            <table className='warning-container'>
                <thead>
                    <tr>
                        <th>Date</th>
                        <th>Ticker</th>
                        <th>Prediction</th>
                        <th>Summary Earnings</th>
                    </tr>
                </thead>
                <tbody>
                    {selectedTickers.map(ticker => (
                        warnings[ticker.value] ? (
                            <tr key={ticker.value}>
                                <td>{warningDates[ticker.value]}</td>
                                <td className='warning-ticker'>{ticker.label}</td>
                                <td>
                                    Potential {warnings[ticker.value].Prediction ? `${(warnings[ticker.value].Prediction * 100).toFixed(1)}%` : 'N/A'} 
                                    {warnings[ticker.value].Prediction > 0 ? <AiOutlineArrowUp className="prediction-positive" /> : <AiOutlineArrowDown className="prediction-negative" />}
                                </td>
                                <td className='summary-earnings'>{warnings[ticker.value].Summary}</td>
                            </tr>
                        ) : null
                    ))}
                </tbody>
            </table>
    );
};

export default LatestWarn;
