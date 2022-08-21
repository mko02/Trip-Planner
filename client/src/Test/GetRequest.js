import fetch from 'node-fetch'

async function doGET() {
    let url = 'http://localhost:8080'
    try {
        let response = await fetch(url)
        console.log(response.headers)
        return await response.json()
    } catch (error) {
        console.log(error)
    }
}

async function GetRequest() {
    let data = await doGET()
    console.log(data.text)
}

await GetRequest()