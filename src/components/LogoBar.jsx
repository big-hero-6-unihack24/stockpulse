import React from "react";
import { PiPulseFill } from "react-icons/pi";
import "../styles.css";

function LogoBar() {
    return (

        <div className="logo-container">
            <div className="logo">
                <h3>
                    <span className="logo-icon"><PiPulseFill/></span>
                    <span className="stock-pulse">STOCKPULSE</span>
                </h3>

            </div>

        </div>

    )
}

export default LogoBar;