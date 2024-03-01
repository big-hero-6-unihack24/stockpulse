import React from "react";
import { BsApp } from "react-icons/bs";
import { HiOutlineArrowSmDown } from "react-icons/hi";
import { TfiTrash } from "react-icons/tfi";
import { FcGoogle } from "react-icons/fc";
import { BsApple } from "react-icons/bs";

import { LuPen } from "react-icons/lu";
import "../styles.css";

class TrackingForm extends React.Component {
    render() {
        return (
            <div>
                <table className="table-container">
                    <tr>
                        <th><BsApp /></th>
                        <th>Name</th>
                        <th>Symbol <HiOutlineArrowSmDown /></th>
                    </tr>
                    <tr>
                        <td><BsApp /></td>
                        <td className="td-name">
                            <div><FcGoogle  size={16}/> </div>
                            <div>Google</div>
                        </td>
                        <td className="symbol">GOOG</td>
                        <td><TfiTrash /></td>
                        <td><LuPen /></td>
                    </tr>
                    <tr>
                        <td><BsApp /></td>
                        <td className="td-name">
                            <div><BsApple size={16}/> </div>
                            <div>Apple</div>
                        </td>
                        <td className="symbol">APPL</td>
                        <td><TfiTrash /></td>
                        <td><LuPen /></td>
                    </tr>
  
                </table>
            </div>
        )

    }
}
export default TrackingForm;