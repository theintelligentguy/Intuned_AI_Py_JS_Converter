import logging
import sys
import os
from dotenv import load_dotenv
import asyncio
from main import main

load_dotenv()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        logging.error("Exactly 1 argument")
        print("Usage: python convert.py <NAME_OF_TEST>")
        sys.exit(1)
    
    try:
        name_of_test = sys.argv[1]
        python_project_location = os.path.join("tests", name_of_test, "py")
        js_project_output_location = os.path.join("tests",name_of_test, "js")
        
        asyncio.run(main(python_project_location, js_project_output_location))
    except ValueError:
        logging.error("Invalid input: Please provide valid arugments")
        sys.exit(1)
