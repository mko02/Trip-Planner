import React from 'react'
import {IconButton, Button} from '@mui/material'
import {Delete} from '@mui/icons-material'
import './Member.css'
function Member(props) {
    // props.members
    // props.onChange
    let member_list = []
    member_list.push(
        <Button className={"add-member-button"} sx={{
            backgroundColor: "#EEEEEE",
            color: "black",
            fontFamily: 'Roboto',
            fontWeight: "300",
            fontSize: "20px",
            paddingTop: "16px",
            paddingBottom: "16px",
        }}>
            Add Member
        </Button>
    );
    for (let m of props.members) {
        member_list.push(
            <div className={"member-package"}>
                <div style={{color: m.color}} className={"member"}>{m.name}</div>
                <IconButton className={"delete-member-button"}>
                    <Delete/>
                </IconButton>
            </div>
        )
    }
    return (
        <div>
            <div>
                <h1>Members</h1>
            </div>
            <div className={"member-list"}>
                {member_list}
            </div>
        </div>
    )
}

export default Member