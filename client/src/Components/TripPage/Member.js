import React, {useState} from 'react'
import {IconButton, Button, Box} from '@mui/material'
import { Delete } from '@mui/icons-material'
import styled from "styled-components";
import TodoList from './Members/MemberList'


import './Member.css'


function Member(props) {
    // props.members
    // props.onChange
    const { members } = props //deconstructions

    const [mems, setmems] = useState(members)
    const [input, setinput] = useState("")

    let member_list = []
    
    // const handleAddMemSubmit = e, => {
    //     e.preventDefault();
    // }

    // const handleAdd = (e, input) => {
    //     e.preventDefault();

    //     console.log(input)
    //     console.log('submit')
    //     setinput("");
        
    // }
    const addmem = mem => {
        const newmembers = [mem, ...mems];

        setmems(newmembers);
        console.log(...mems);
      };
    
    const removemem = id => {
        const removedArr = [...mems].filter(mem => mem.id !== id);
    
        setmems(removedArr);
      };
    // member_list.push(
    //     <Button className={"add-member-button"} sx={{
    //         backgroundColor: "#EEEEEE",
    //         color: "black",
    //         fontFamily: 'Roboto',
    //         fontWeight: "300",
    //         fontSize: "20px",
    //         paddingTop: "16px",
    //         paddingBottom: "16px",
    //     }}>
    //         Add Member
    //     </Button>
    // );
    // for (let m of props.members) {
    //     member_list.push(
    //         <div className={"member-package"}>
    //             <div style={{color: m.color}} className={"member"}>{m.name}</div>
    //             <IconButton className={"delete-member-button"}>
    //                 <Delete/>
    //             </IconButton>
    //         </div>
    //     )
    // }
    return (
        <div>
            <div className='title'>
                Members
            </div>
            <form className='addmem-form' onSubmit={addmem}>
                <SearchInput
                    type="text"
                    placeholder='Member Name'
                    onChange={(e) => setinput(e.target.value)}
                > 
                    {console.log(input)}
                </SearchInput>
                <Button onClick={addmem}  sx ={{bgcolor:"pink"}}> Add</Button>
            </form>

            <div className={"member-list"}>
                {member_list}
                {mems.map((each_mem) => (
                    <Box>{each_mem.name}</Box>
                ))}
            </div>
        </div>
    )
}

export default Member

const SearchInput = styled.input`
  background: yellow;
  border: 0.25em solid;
  border-color: black;
  border-radius: 2px;
  width: 40%;
  color: black;
`;
