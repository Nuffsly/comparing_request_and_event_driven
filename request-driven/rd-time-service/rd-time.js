const app = require("express")();

app.get("/", (request, response) => {
    let now = new Date();

    response.json({"hour":now.getHours(), "minute":now.getMinutes(), "second":now.getSeconds()})
})

const port = 8001;

app.listen(port, () => console.log(`time-service listening on http://localhost:${port}`))