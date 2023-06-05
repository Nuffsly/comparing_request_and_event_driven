const app = require("express")();
const amqp = require("amqplib/callback_api");

let time = {"hour":0, "minute":0, "second":0};
let count = {"count":0};
let apiChannel;


amqp.connect('amqp://user:pass@definition', function(error0, connection) {
    if (error0){
        throw error0;
    }
    // Start listening to time queue.
    connection.createChannel(function(error1, channel) {
        if(error1) {
            throw error1;
        }
        let queue = 'time';

        channel.assertQueue(queue, {
            durable: true
        });

        console.log(" [*] Listening for messages in %s.", queue);

        channel.consume(queue, function(msg) {
            time = JSON.parse(msg.content.toString());
            channel.ack(msg);
        }, {
            noAck: false
        });
    });

    // Start listening to count queue
    connection.createChannel(function(error1, channel) {
        if(error1) {
            throw error1;
        }
        let queue = 'count';

        channel.assertQueue(queue, {
            durable: true
        });

        console.log(" [*] Listening for messages in %s.", queue);

        channel.consume(queue, function(msg) {
            count = JSON.parse(msg.content.toString());
            channel.ack(msg);
        }, {
            noAck: false
        });
    });

    // Connect to API channel to send messages.
    connection.createChannel(function(error1, channel) {
        if(error1) {
            throw error1;
        }
        let queue = 'api';

        channel.assertQueue(queue, {
            durable: true
        });

        apiChannel = channel;
    });
});

app.get("/", (request, response) => {
    response.json({message: `The time is currently: ${time.hour}:${time.minute}:${time.second}\n And the count is ${count.count}`})
    try {apiChannel.sendToQueue('api', Buffer.from('API requested'));}
    catch(err){
        throw err;
    }
})

const port = 8000;

app.listen(port, () => console.log(`app listening on http://localhost:${port}`))