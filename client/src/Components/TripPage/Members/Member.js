import React, { useState } from 'react';
import NewMemberForm from './NewMemberForm';
import { Delete } from '@mui/icons-material'
import { Typography, Box } from '@mui/material'
import styled from "styled-components"


const Member = ({ members, removemem }) => {
    return members.map((member) => (
        <Memberdiv>
            <Box sx={{border: "solid"}}>
                <Typography sx={{color:member.color}}>{member.name}</Typography>
            </Box>
            <Delete
                onClick={() => removemem(member.name)}
                className='delete-icon'
                />
        </Memberdiv>
    ));
};

export default Member;

const Memberdiv = styled.div`
 border: black solid "1px";
`