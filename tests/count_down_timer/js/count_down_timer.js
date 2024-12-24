function countdown(start) {
    let timer = setInterval(() => {
        console.log(`Countdown: ${start}`);
        start--;
        
        if (start < 0) {
            clearInterval(timer);
            console.log("Time's up!");
        }
    }, 1000);
}

let startNumber = parseInt(prompt("Enter the starting number for the countdown:"));
countdown(startNumber);