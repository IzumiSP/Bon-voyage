const { Client } = require('pg');

const client = new Client({
    user: 'postgres',
    host: 'localhost',

    database: 'my_database',
    password: 'qwerty',
    port: 5432,
});

client.connect()
.then(() => console.log('Connected to PostgreSQL'))
.catch(err => console.error('Connection error', err.stack));

module.exports = client;