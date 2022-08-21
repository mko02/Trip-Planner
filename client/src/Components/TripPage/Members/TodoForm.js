import React, { useState, useEffect, useRef } from 'react';

function TodoForm(props) {
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
            id: input,
            color: 'black'
        })
        setInput('');
    };

    return (
    <form onSubmit={handleSubmit} className='todo-form'>
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
    </form>
    );
    }

    export default TodoForm;