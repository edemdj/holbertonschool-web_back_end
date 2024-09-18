// Display welcome message
console.log('Welcome to Holberton School, what is your name?');

// Listen for user input on stdin
process.stdin.on('data', (input) => {
  const name = input.toString().trim();
  console.log(`Your name is: ${name}`);

  // Close the program with the message
  console.log('This important software is now closing');

  // Exit the process
  process.exit();
});
