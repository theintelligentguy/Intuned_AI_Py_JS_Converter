def print_fancy_hello():
    # The ASCII art letters for "Hello!"
    hello = """
    ##     ##  #######  ##       ##        #######           
    ##     ## ##        ##       ##       ##     ##          
    ##     ## ##        ##       ##       ##     ##          
    ######### #######   ##       ##       ##     ##          
    ##     ## ##        ##       ##       ##     ##          
    ##     ## ##        ##       ##       ##     ##          
    ##     ##  #######  ######## ########  #######   
    """
    
    # Add some simple animation by printing with different characters
    import time
    import os
    
    chars = ['*', '#', '@', '$', '%']
    
    for char in chars:
        # Clear console (works on both Windows and Unix-like systems)
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Replace the # with different characters each time
        current_pattern = hello.replace('#', char)
        print(current_pattern)
        time.sleep(0.3)

print_fancy_hello()