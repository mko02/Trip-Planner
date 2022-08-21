import React, { useState, useEffect, useRef } from 'react';
import { Stack } from '@mui/material';


function NewMemberForm(props) {
const [input, setInput] = useState(props.edit ? props.edit.value : '');
    const inputRef = useRef(null);

    useEffect(() => {
    inputRef.current.focus();
    });

    const handleChange = e => {
    setInput(e.target.value);
    };

    const handleSubmit = e => {
        e.preventDefault();

        props.onSubmit({
            name: input,
            color: 'black'
        })
        setInput('');
    };

    return (
    <form onSubmit={handleSubmit} className='todo-form'>
        <Stack direction="row">
            <input
                placeholder='Add a todo'
                value={input}
                onChange={handleChange}
                name='text'
                className='todo-input'
                ref={inputRef}
            />
            <button onClick={handleSubmit} className='todo-button'>
            Add 
                </button>
        </Stack>
        
    </form>
    );
    }

export default NewMemberForm;