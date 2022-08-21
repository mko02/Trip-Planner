import React, { useState, useEffect, useRef } from 'react';
import { Stack, Button } from '@mui/material';
import styled from "styled-components"
import { CirclePicker } from 'react-color';


function NewMemberForm(props) {
    const [input, setInput] = useState(props.edit ? props.edit.value : '');
    const [color, setColor] = useState('#000000');
    const [showColorPicker, setShowColorPicker] = useState(false);

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
            color: color,
        })
        setInput('');
    };

    return (
    <form onSubmit={handleSubmit} className='todo-form'>
        <Formdiv>
            { showColorPicker && 
                <CirclePicker 
                color={color} 
                onChange={updateColor => setColor(updateColor.hex)}
                sx={{
                    margin: '100px',
                    padding: '100px'
                }}
                />
            }
            <NewMemberInput
                placeholder='Add a Member'
                value={input}
                onChange={handleChange}
                name='text'
                className='todo-input'
                ref={inputRef}
            />
            <Button
                onClick={() => setShowColorPicker(showColorPicker => !showColorPicker)}
                variant='contained'
                disableElevation
                disableRipple
                sx={{
                    backgroundColor: color,
                    borderRadius: 35,
                    minWidth: '30px',
                    maxWidth: '30px',
                    height: '30px',
                    marginRight: '0',
                    marginLeft: '15px',
                    shadow: 'none',
                    "&.MuiButtonBase-root:hover": {
                        background: color,
                    }
                }}>
                
            </Button>
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
    width: 150px;
`
const Formdiv = styled.div`
flex-direction: row;
`
