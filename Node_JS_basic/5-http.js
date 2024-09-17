const http = require('http');
const url = require('url');
const countStudents = require('./3-read_file_async');
const fs = require('fs');


const app = http.createServer((req, res) => {
  const parsedUrl = url.parse(req.url, true);


  res.writeHead(200, { 'Content-Type': 'text/plain' });

  if (parsedUrl.pathname === '/') {
    res.end('Hello Holberton School!');
  } else if (parsedUrl.pathname === '/students') {
    res.write('This is the list of our students\n');

    const databasePath = process.argv[2];

    if (fs.existsSync(databasePath)) {
      countStudents(databasePath)
        .then(() => res.end())
        .catch((err) => {
          res.write(err.message);
          res.end();
        });
    } else {
      res.write('Cannot load the database');
      res.end();
    }
  } else {

    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('404 Not Found');
  }
});

app.listen(1245, () => {
  console.log('Server is listening on port 1245');
});

module.exports = app;
