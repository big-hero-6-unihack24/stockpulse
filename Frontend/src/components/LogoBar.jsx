import React, { useState } from "react";
import { PiPulseFill } from "react-icons/pi";
import { LuPen } from "react-icons/lu";
import "../styles.css";
import axios from 'axios';

function LogoBar() {
    const [email, setEmail] = useState('email@gmail.com');
    const [isEditing, setIsEditing] = useState(false);

   const handleEmailChange =(e) => {
    setEmail(e.target.value)
   }

   const updateEmail = async () => {
        try {
            const url = 'https://stockpulse-api.azurewebsites.net/update-email';
            const payload = { email: email };
            await axios.post(url, payload);
            console.log('Email updated successfully');
        } catch (error) {
            console.error('Error updating email:', error);
        }
   };


   const saveEmail = () => {
    setIsEditing(false);
    updateEmail()
   }

   const enableEdit = () => {
    setIsEditing(true);
   }
    return (

        <div className="logo-container">
            <div className="logo">
                <h3>
                    <span className="logo-icon"><PiPulseFill/></span>
                    <span className="stock-pulse">STOCKPULSE</span>
                </h3>

            </div>
            <div className="user-email">
                {isEditing ? (
                    <div><input
                            className="email-input"
                            type="text"
                            value={email}
                            onChange={handleEmailChange}
                            onBlur={saveEmail}
                            onKeyPress={(e) => e.key === 'Enter' && saveEmail()}


                        />
                    </div>
                ) : (
                    <>
                    <div className="email">{email}</div>
                    <div onClick={enableEdit}><LuPen/></div>
                    </>

                )}
                

            </div>

        </div>

    )
}

export default LogoBar;
