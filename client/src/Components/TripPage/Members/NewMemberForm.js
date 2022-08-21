import React, { useState, useEffect, useRef } from 'react';
import { Stack, Button } from '@mui/material';
import styled from "styled-components"


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
        <Formdiv>
            <NewMemberInput
                placeholder='Add a Member'
                value={input}
                onChange={handleChange}
                name='text'
                className='todo-input'
                ref={inputRef}
            />
            <Button onClick={handleSubmit} className='todo-button'> Add </Button>
        </Formdiv>
        
    </form>
    );
    }

export default NewMemberForm;

const NewMemberInput = styled.input`
    border-radius: 5px;
    border-width: 0.25px;
    padding:8px;
`
const Formdiv = styled.div`
flex-direction: row;
`
