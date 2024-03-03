import React, { useState } from "react";
import LogoBar from "./LogoBar";
import Header from "./Header";
import Input from "./Input";
import Dashboard from "./Dashboard";
import axios from 'axios';

function App() {

    const [selectedTickers, setSelectedTickers] = useState([]);

    const addSelectedTicker = ticker => {

        if (!selectedTickers.some(selected => selected.value === ticker.value)) {
            setSelectedTickers(prevTickers => [...prevTickers, ticker]);
        }
        
    }
    return (
        <div class="master-container">
            <LogoBar/>
            <Header tagline="Revolutionize your investments with real-time, data-driven insights and alerts on the stock movements post-earnings."/>
            <Input addSelectedTicker={addSelectedTicker}/>
            <Dashboard selectedTickers={selectedTickers}/>

        </div>
    )
}

export default App;
