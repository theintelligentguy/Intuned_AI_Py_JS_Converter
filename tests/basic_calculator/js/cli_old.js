// example of how to import
// import fetch from "node-fetch";


/**
 * Add two numbers and log the operation details.
 *
 * @param {number} a - First number
 * @param {number} b - Second number
 * @returns {number} Sum of the two numbers
 */
function addNumbers(a, b) {
  console.log(`Starting addition operation with inputs: ${a} and ${b}`);

  try {
    const result = a + b;
    console.log(`Successfully calculated sum: ${result}`);
    return result;
  } catch (error) {
    console.log(`Error during addition: ${error.message}`);
    throw error;
  }
}

// Get command line arguments (skip first two as they are node and script path)
const args = process.argv.slice(2);

// Check if correct number of arguments are provided
if (args.length !== 2) {
  console.log("Exactly 2 numbers are required as arguments");
  console.log("Usage: node script.js <number1> <number2>");
  process.exit(1);
}

try {
  // Convert command line arguments to numbers
  const num1 = parseFloat(args[0]);
  const num2 = parseFloat(args[1]);

  // Check if the conversion was successful
  if (isNaN(num1) || isNaN(num2)) {
    throw new Error("Invalid input: Please provide valid numbers");
  }

  // Calculate and print result
  const result = addNumbers(num1, num2);
  console.log(`Sum: ${result}`);
} catch (error) {
  console.log(error.message);
  console.log("Error: Please provide valid numbers");
  process.exit(1);
}
