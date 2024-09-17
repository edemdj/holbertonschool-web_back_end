const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    // Asynchronously read the file
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        // If there is an error, reject the promise with an error message
        reject(new Error('Cannot load the database'));
      } else {
        // Process the data
        const lines = data.trim().split('\n').filter(line => line.trim() !== ''); // Filter out empty lines

        if (lines.length <= 1) {
          reject(new Error('Cannot load the database'));
        } else {
          // Extract the student data
          const students = lines.slice(1).map(line => line.split(','));

          // Log the total number of students
          console.log(`Number of students: ${students.length}`);

          // Group students by field and collect first names
          const fields = {};
          students.forEach(student => {
            const field = student[3]; // Assuming field of study is in the 4th column
            const firstName = student[0]; // Assuming first name is in the 1st column

            if (!fields[field]) {
              fields[field] = [];
            }
            fields[field].push(firstName);
          });

          // Log number of students in each field and their names
          for (const [field, firstNames] of Object.entries(fields)) {
            console.log(`Number of students in ${field}: ${firstNames.length}. List: ${firstNames.join(', ')}`);
          }

          resolve();
        }
      }
    });
  });
}

module.exports = countStudents;
