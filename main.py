import asyncio
import os
from dotenv import load_dotenv
import anthropic
from modules.batch_processing import process_batch_results
from modules.validation import validate_code  # Import validation module

def read_python_files(path_py_project):
    """
    Read all Python files from the folder.
    """
    return [f for f in os.listdir(path_py_project) if f.endswith('.py') and os.path.isfile(os.path.join(path_py_project, f))]

async def main(path_py_project: str, path_js_project: str):
    """
    Batch conversion handler.
    """
    print(f"Python project to convert - {path_py_project}")
    print(f"JS project output location - {path_js_project}")

    # Load environment variables from .env.example
    env_path = os.path.join(os.getcwd(), '.env.example')
    load_dotenv(dotenv_path=env_path)

    # Create anthropic client from a valid API key
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    if not client:
        raise ValueError("Anthropic client initialization failed. Check your API key.")

    # Read all Python files in the folder
    python_files = read_python_files(path_py_project)
    if not python_files:
        print("No Python files found to process.")
        return

    # Prepare batch requests
    requests = []
    for python_file in python_files:
        path_py_file = os.path.join(path_py_project, python_file)
        with open(path_py_file, 'r') as f:
            python_code = f.read()

        prompt = f"""
        The following is a single Python file code. Convert the code inside the file into JavaScript code.
        If the contents of the file are not Python code, return only the message 'Not Python Code', 
        otherwise, return only the converted code and do not add any dialog. 
        The file:
        {python_code}
        """

        custom_id = os.path.splitext(python_file)[0]
        requests.append(
            anthropic.types.messages.batch_create_params.Request(
                custom_id=custom_id,
                params=anthropic.types.message_create_params.MessageCreateParamsNonStreaming(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=8192,
                    messages=[{"role": "user", "content": prompt}]
                )
            )
        )

    # Send batch requests
    try:
        batch_response = client.messages.batches.create(requests=requests)
        if not batch_response or not batch_response.id:
            raise ValueError("Batch response is invalid or missing an ID.")

        # Process batch results
        await process_batch_results(client, batch_response.id, path_js_project, python_files)

        # Validate the converted JavaScript files
        print("\nValidating converted JavaScript files against original Python files...")
        for python_file in python_files:
            python_path = os.path.join(path_py_project, python_file)
            js_file_name = os.path.splitext(python_file)[0] + ".js"
            js_path = os.path.join(path_js_project, js_file_name)
            
            # Call validation logic
            validate_code(client, python_path, js_path)
    except Exception as e:
        print(f"An error occurred during batch processing: {e}")
