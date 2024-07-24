import divideFunction from './8-try';

try {
  console.log(divideFunction(10, 2)); // Should print 5
} catch (error) {
  console.error(error.toString());
}

try {
  console.log(divideFunction(10, 0)); // Should throw an error
} catch (error) {
  console.error(error.toString());
}
