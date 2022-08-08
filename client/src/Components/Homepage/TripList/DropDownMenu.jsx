import React from 'react'
import './Trip.css'

export default function DropDownMenu() {

    function DropDownItems(props) {
        return (
            <div  className='dropDownItems'>
                {props.children}
            </div>

        )
    }

  return (
    <div>
        <DropDownItems>Share</DropDownItems>
        <DropDownItems>Delete</DropDownItems>
    </div>
  )
}
