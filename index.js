const express = require('express');
const app = express();

app.use('/', (req, res) => {
    res.json({'it': 'works!'});
});

const appPort = process.env.PORT || 8765;

app.listen(appPort, err => {
    if (err) {
        console.error('Не удалось запустить сервер:');
        console.error(err);
        return;
    }

    console.log(`Сервер запущен на ${appPort} порту`);
});
