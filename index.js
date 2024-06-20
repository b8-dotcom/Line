const express = require('express');
const line = require('@line/bot-sdk');

const config = {
  channelAccessToken: '3N+hwqKvNK8MUNVrV4EeboNrD/1liUCyq30MZ241s1BDNKRie2hMywwMBquG72uqVFdQZqL+/TcqsO5sD2De5abt841S4Fb79Y0khqBCIe1jWsVW/JTxlabWkjoYdFfa8zcxOuPhJnjVIb3SJ+fhGwdB04t89/1O/w1cDnyilFU=', // 更新為你的 Channel Access Token
  channelSecret: '93a8d88c1459c647e0a80e3ea21d95b8'  // 更新為你的 Channel Secret
};

const app = express();

// 設置 Line Bot 的 Webhook 路由
app.post('/webhook', line.middleware(config), (req, res) => {
  Promise
    .all(req.body.events.map(handleEvent))
    .then((result) => res.json(result))
    .catch((err) => {
      console.error('Error processing events:', err);
      res.status(500).end();
    });
});

// 處理 Line Bot 的事件
function handleEvent(event) {
  if (event.type !== 'message' || event.message.type !== 'text') {
    return Promise.resolve(null);
  }

  // Echo back the text message
  const client = new line.Client(config);
  return client.replyMessage(event.replyToken, {
    type: 'text',
    text: event.message.text
  });
}

const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
 
