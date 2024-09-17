const express = require('express');
const countStudents = require('./3-read_file_async');
const fs = require('fs');

const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  const databasePath = process.argv[2];

  if (!databasePath) {
    return res.status(500).send('Database file path not provided');
  }

  if (!fs.existsSync(databasePath)) {
    return res.status(500).send('Cannot load the database');
  }

  res.write('This is the list of our students\n');

  countStudents(databasePath)
    .then(() => {
      res.end();
    })
    .catch((err) => {
      res.status(500).send(err.message);
    });
});

app.listen(1245, () => {
  console.log('Server is listening on port 1245');
});

module.exports = app;
