import fetch from 'node-fetch'
import {sample_trip} from "../DummyInfo/sample_trip.js"

async function doPOST() {
    let url = 'http://localhost:8080'
    try {
        let response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(sample_trip)
        })
        console.log(response.headers)
        return await response.text()
    } catch (error) {
        console.log(error)
    }
}

async function PostRequest() {
    let response = await doPOST()
    console.log(response)
}

PostRequest()