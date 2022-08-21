import React, { useState } from 'react';
import TodoForm from './TodoForm';
import Todo from './Todo';

function TodoList(props) {
    const { members } = props
    const [listmembers, setlistmembers] = useState(members);
    console.log('listmembers',listmembers)
    //console.log('members', members)
    //console.log('member', members.map((mem) => { console.log(mem)}))
    // const {name, color} = 

    const addmen = mem => {
        console.log('addmen', mem)
        const newlistmembers = [mem, ...listmembers];
        console.log('newlistmember', newlistmembers)
        setlistmembers(newlistmembers);
        console.log('currentlistmembers', listmembers);
    };

    // const removemem = id => {
    // const removedArr = [...members].filter(todo => todo.id !== id);

    // setlistmembers(removedArr);
    // };


    return (
    <>
        <TodoForm onSubmit={addmen} />
        <Todo
        members={members}
        // removeTodo={removeTodo}
        />
    </>
    );
    }

export default TodoList;
