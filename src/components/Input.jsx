import React from "react";
import "../styles.css";

function Input() {
    return (
        <div className="input-bar">
            <span><input className="ticker" type="text" placeholder="Enter your ticker here..."></input></span>
            <span><input className="threshold" type="text" placeholder="What is your threshold?..."></input></span>
            <span><button>Submit</button></span>


        </div>
    )
}

export default Input;