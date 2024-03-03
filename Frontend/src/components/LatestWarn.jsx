import React, { useState, useEffect } from 'react';
import "../styles.css";
import axios from 'axios';
import { AiOutlineArrowUp } from "react-icons/ai";
import { AiOutlineArrowDown } from "react-icons/ai";
const LatestWarn = () => {
    const [warning, setWarning] = useState(null);
    const [warningDate, setWarningDate] = useState('');

    const ticker = 'META'; 
    const threshold = 0.001;

    useEffect(() => {
        const fetchWarning = async () => {
            try {
                const url = `${process.env.REACT_APP_BACKEND_URL}/warning?ticker=${ticker}&threshold=${threshold}`;
                const response = await axios.get(url);
                if (response.data) {
                    setWarning(response.data);
                    setWarningDate(new Date().toLocaleDateString());
                }
            } catch (error) {
                console.error('Error fetching warning: ', error);
            }
        };
        fetchWarning();
    }, [ticker, threshold]); 

    const predictionValue = warning && warning.Prediction ? (warning.Prediction * 100).toFixed(1) : 'N/A';

    const renderPredictionIcon = (prediction) => {
        if (prediction > 0) {
            return  <AiOutlineArrowUp className="prediction-positive" />;
        } else {
            return <AiOutlineArrowDown className="prediction-negative" />;
        } 
    };

    return (
        <div className="warning">
            <div className='warning-day'>
                <div><h3>Latest warning</h3></div>
                <div><p>{warningDate}</p></div>
            </div>
        
            {warning && (
                <div className="warning-infor">
                    <div className="warning-ticker"><h3>{ticker}</h3></div>
                        {/* <p>Potential {warning.Prediction ? `${(warning.Prediction * 100).toFixed(1)}%` : 'N/A'} </p> */}
                       <div className="warning-potential"><p className="prediction-value">Potential {predictionValue}% {renderPredictionIcon(warning.Prediction)}</p></div>

                    <div className="warning-sum">
                        <div><h3>Summary Earnings </h3></div>
                        <div><p>{warning.Summary}</p></div>
                    </div>
                </div>
            )}
        </div>
    );
};

export default LatestWarn;
