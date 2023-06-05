const amqp = require("amqplib/callback_api");

amqp.connect("amqp://user:pass@definition", function (error0, connection) {
  if (error0) {
    throw error0;
  }
  connection.createChannel(function (error1, channel) {
    if (error1) {
      throw error1;
    }
    let apiQueue = "api";
    let countQueue = "count";
    let connectionCount = 0;

    channel.assertQueue(apiQueue, {
      durable: true,
    });
    channel.consume(apiQueue, function (msg) {
      channel.assertQueue(countQueue, {
        durable: true,
      });
      ++connectionCount;
      channel.sendToQueue(
        countQueue,
        Buffer.from(JSON.stringify({ count: connectionCount }))
      );
      channel.ack(msg);
    }, {
        noAck: false
    });
  });
});
