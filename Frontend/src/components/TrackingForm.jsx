import React from "react";
import { BsApp } from "react-icons/bs";
import { HiOutlineArrowSmDown } from "react-icons/hi";
import { TfiTrash } from "react-icons/tfi";

import { LuPen } from "react-icons/lu";
import "../styles.css";

class TrackingForm extends React.Component {
    render() {
        const { selectedTickers } = this.props;
        return (
            <div>
                <table className="table-container">
                    <tr>
                        <th><BsApp /></th>
                        <th>Name</th>
                        <th>Symbol <HiOutlineArrowSmDown /></th>
                    </tr>
                    {selectedTickers.map((ticker, index) => (
                        <tr key={index}>
                        <td><BsApp /></td>
                        <td className="td-name">
                            <div>{ticker.icon} </div>
                            <div>{ticker.label}</div>
                        </td>
                        <td className="symbol">{ticker.value}</td>
                        <td><TfiTrash /></td>
                        <td><LuPen/></td>

                        </tr>
                    ))}
  
                </table>
            </div>
        )

    }
}
export default TrackingForm;
