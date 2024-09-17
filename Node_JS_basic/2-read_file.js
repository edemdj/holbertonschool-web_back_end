const fs = require('fs');

function countStudents(path) {
  try {
    // Read the CSV file synchronously
    const data = fs.readFileSync(path, 'utf-8').trim();

    // Split the data by newline to get rows
    const rows = data.split('\n').filter((row) => row.trim() !== ''); // Filter out any empty lines

    if (rows.length <= 1) {
      throw new Error('Cannot load the database');
    }

    // Extract header and student data
    const headers = rows[0].split(',');
    const students = rows.slice(1).map(row => row.split(','));

    // Count total number of students
    console.log(`Number of students: ${students.length}`);

    // Group students by their field of study
    const fields = {};
    students.forEach(student => {
      const field = student[3]; // Assuming the field of study is in the 4th column
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

  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
