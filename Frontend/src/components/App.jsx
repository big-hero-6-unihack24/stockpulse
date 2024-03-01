import React from "react";
import LogoBar from "./LogoBar";
import Header from "./Header";
import Input from "./Input";
import Dashboard from "./Dashboard";
import axios from 'axios';

function App() {
    return (
        <div>
            <LogoBar/>
            <Header tagline="Revolutionize your investments with real-time, data-driven insights and alerts on the stock movements post-earnings."/>
            <Input/>
            <Dashboard/>

        </div>
    )
}

export default App;