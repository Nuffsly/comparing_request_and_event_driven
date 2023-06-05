const amqp = require('amqplib/callback_api');

function currentTime() {
    let now = new Date();
    return JSON.stringify({"hour":now.getHours(), "minute":now.getMinutes(), "second":now.getSeconds()});
}

amqp.connect('amqp://user:pass@definition', function(error0, connection) {
    if (error0){
        throw error0;
    }
    connection.createChannel(function(error1, channel) {
        if(error1) {
            throw error1;
        }
        let queue = 'time';

        channel.assertQueue(queue, {
            durable: true
        });
        setInterval(function(){channel.sendToQueue(queue, Buffer.from(currentTime()))}, 100);
    });
});