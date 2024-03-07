import React from "react";
import { BsApp } from "react-icons/bs";
import { TfiTrash } from "react-icons/tfi";
import "../styles.css";

class TrackingForm extends React.Component {
    render() {
        const { selectedTickers =[], removeTicker } = this.props;
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
                        <td><TfiTrash onClick={() => removeTicker(ticker.value)}/></td>
                    

                        </tr>
                    ))}
  
                </table>
         
        )

    }
}
export default TrackingForm;
