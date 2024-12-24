
// cli_no_args.js

function main() {
    console.log("Hello from a Python CLI with no arguments!");
}

if (require.main === module) {
    main();
}