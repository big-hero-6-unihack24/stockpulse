import React from "react";
import { BsApp } from "react-icons/bs";
import { TfiTrash } from "react-icons/tfi";

import { LuPen } from "react-icons/lu";
import "../styles.css";

class TrackingForm extends React.Component {
    render() {
        const { selectedTickers =[] } = this.props;
        return (
            
                <table className="table-container">
                    <tr>
                        <th><BsApp /></th>
                        <th>Name</th>
                        <th>Symbol</th>
                    </tr>
                    {selectedTickers.map((ticker, index) => (
                        <tr key={index}>
                        <td><BsApp /></td>
                        <td>{ticker.label}</td>
                        <td className="symbol">{ticker.value}</td>
                        <td><TfiTrash /></td>
                        <td><LuPen/></td>

                        </tr>
                    ))}
  
                </table>
         
        )

    }
}
export default TrackingForm;
