import React, { useState } from 'react'

export default function DropDown(props) {

    const [open, setOpen] = useState(false);

    function DropDownItem(props) {
        
    }

  return (
    <div onClick={() => setOpen(!open)}>
        {props.icon}

        {open && props.children}
    </div>
  )
}
