// cli_with_args.js
function main() {
    if (process.argv.length < 3) {
        console.log("Usage: node cli_with_args.js <name>");
        return;
    }

    const name = process.argv[2];
    console.log(`Hello, ${name}! Welcome to the JavaScript CLI.`);
}

main();