function printFancyHello() {
    // The ASCII art letters for "Hello!"
    const hello = `
    ##     ##  #######  ##       ##        #######           
    ##     ## ##        ##       ##       ##     ##          
    ##     ## ##        ##       ##       ##     ##          
    ######### #######   ##       ##       ##     ##          
    ##     ## ##        ##       ##       ##     ##          
    ##     ## ##        ##       ##       ##     ##          
    ##     ##  #######  ######## ########  #######   
    `;
    
    const chars = ['*', '#', '@', '$', '%'];
    
    for (let char of chars) {
        // Clear console
        console.clear();
        
        // Replace the # with different characters each time
        const currentPattern = hello.replace(/#/g, char);
        console.log(currentPattern);
        
        // Sleep for 300ms
        new Promise(resolve => setTimeout(resolve, 300));
    }
}

printFancyHello();