import React, { useState } from 'react';
import TodoForm from './TodoForm';
import { Delete } from '@mui/icons-material'
import {Typography, Box} from '@mui/material'


const Todo = ({ members, removeTodo }) => {
    return members.map((member) => (
        <div className='icons'>
            <Box>
                <Typography sx={{color:member.color}}>{member.name}</Typography>
            </Box>
            <Delete
                onClick={() => removeTodo(member.name)}
                className='delete-icon'
                />
        </div>
    ));
};

export default Todo;