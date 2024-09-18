import fs from 'fs/promises';

export async function readDatabase(filePath) {
  try {
    const data = await fs.readFile(filePath, 'utf-8');
    const lines = data.split('\n').filter(line => line !== ''); // Ignore empty lines
    const fields = {};

    // Process the CSV lines (assuming the format is Firstname,Lastname,Field)
    for (let i = 1; i < lines.length; i++) {
      const [firstname, , field] = lines[i].split(',');
      if (firstname && field) {
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      }
    }
    return fields;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}
