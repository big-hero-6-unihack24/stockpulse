import React from "react";
import "../styles.css";
import { SlCloudDownload } from "react-icons/sl";
import { IoAdd } from "react-icons/io5";
import TrackingForm from "./TrackingForm";
import LatestWarn from "./LatestWarn";

function Dashboard({ selectedTickers, setSelectedTickers }) {
     const removeTicker = (tickerValue) => {
        const updateTickers = selectedTickers.filter(ticker => ticker.value !== tickerValue);
        setSelectedTickers(updateTickers);
    }
    return(
        <div className="dashboard-container">
            <div className="dashboard-heading">
                <div className="heading">
                    <h3>
                        <span className="your-dashboard">Your Portfolio</span>
                        {/* <span className="investor-relation">Investor Relation</span> */}
                    </h3>
                </div>
                <div className="heading-button">
                    <h3><span className="your-dashboard">Warnings</span></h3>
                    {/* <span><button className="download"><SlCloudDownload /> Download CSV</button></span>
                    <span><button className="add"><IoAdd /> Add IR</button></span> */}
                </div>

            </div>
            <div className="dashboard-table">
                <TrackingForm selectedTickers={selectedTickers} removeTicker={removeTicker}/>
                <LatestWarn selectedTickers={selectedTickers}/>

            </div>

        </div>
    )
}

export default Dashboard;
