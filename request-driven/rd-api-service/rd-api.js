const app = require("express")();
const axios = require("axios");

app.get("/", async (request, response) => {
    let time;
    let count;

    req1 = axios.get('http://rd-time-service:8001').then(timeRes => {
        time = timeRes.data;
    })

    req2 = axios.get('http://rd-count-service:8002').then(countRes => {
        count = countRes.data.count;
    })

    await req1;
    await req2;

    response.json({message: `The time is currently: ${time.hour}:${time.minute}:${time.second}\n And the count is ${count}`})
})

const port = process.env.PORT || 8000;

app.listen(port, () => console.log(`app listening on http://localhost:${port}`))