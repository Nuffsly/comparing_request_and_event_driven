const app = require("express")();

let counter = 0;

app.get("/", (request, response) => {
    response.json({"count":++counter});
})

const port = 8002;

app.listen(port, () => console.log(`count-service listening on http://localhost:${port}`))