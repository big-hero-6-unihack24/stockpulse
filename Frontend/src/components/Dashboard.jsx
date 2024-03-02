import React from "react";
import "../styles.css";
import { SlCloudDownload } from "react-icons/sl";
import { IoAdd } from "react-icons/io5";
import TrackingForm from "./TrackingForm";
import LatestWarn from "./LatestWarn";

function Dashboard({ selectedTickers }) {
    return(
        <div className="dashboard-container">
            <div className="dashboard-heading">
                <div className="heading">
                    <h3>
                        <span className="your-dashboard">Your Dashboard</span>
                        <span className="investor-relation">Investor Relation</span>
                    </h3>
                </div>
                <div className="heading-button">
                    <span><button className="download"><SlCloudDownload /> Download CSV</button></span>
                    <span><button className="add"><IoAdd /> Add IR</button></span>
                </div>

            </div>
            <div className="dashboard-table">
                <div><TrackingForm selectedTickers={selectedTickers}/></div>
                <div><LatestWarn/></div>

            </div>

        </div>
    )
}

export default Dashboard;
