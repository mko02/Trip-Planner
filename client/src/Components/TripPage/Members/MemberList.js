import React, { useState } from 'react';
import NewMemberForm from './NewMemberForm';
import Member from './Member';

function MemberList(props) {
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

    const removemem = name => {
        const removedArr = [...listmembers].filter(member => member.name !== name);
        setlistmembers(removedArr);
        console.log('tried to remove')
    };


    return (
    <>
        <NewMemberForm onSubmit={addmen} />
        <Member
        members={listmembers}
        removemem={removemem}
        />
    </>
    );
    }

export default MemberList;
