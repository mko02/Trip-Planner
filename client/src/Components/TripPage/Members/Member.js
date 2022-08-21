import React, { useState } from 'react';
import NewMemberForm from './NewMemberForm';
import { Delete } from '@mui/icons-material'
import { Typography, Box } from '@mui/material'
import styled from "styled-components"


const Member = ({ members, removemem }) => {
    return members.map((member) => (
            <Box sx={{border: "solid", borderRadius:1, marginTop:"5%", display:"flex", flexDirection:"row", justifyContent:"space-between", padding:"5px", borderWidth:"0.25px", height: "35%", alignItems: "center"}}>
                <Typography sx={{ color: member.color, paddingLeft:"8px"}}>{member.name}</Typography>
                <Delete
                    onClick={() => removemem(member.name)}
                    sx={{
                    paddingRight:"8px",
                        "&:hover": {
                            cursor: "pointer",
                        }
                    }}
                />
            </Box>
    ));
};

export default Member;
