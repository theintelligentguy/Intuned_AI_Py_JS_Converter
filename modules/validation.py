import subprocess
import anthropic
import os


def generate_test_cases(client, python_code_path: str) -> str:
    """
    Use LLM to generate test cases for the given Python code.
    """
    print("Starting test case generation...")

    # Read the Python code from the file
    try:
        with open(python_code_path, "r") as file:
            python_code = file.read()
    except FileNotFoundError:
        raise ValueError(f"File not found: {python_code_path}")

    # Prompt engineering
    prompt = f"""
    The following is Python code. Generate relevant test cases that test the functionality 
    of the given code. Include input, expected output, and any specific setup or considerations:
    {python_code}
    """

    try:
        # generate test cases
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=8192,
            messages=[{"role": "user", "content": prompt}]
        )
        print("Response received:", response)

        # Directly access the `content` attribute of the response
        if not hasattr(response, "content") or not response.content:
            raise ValueError("Response has no content or is empty.")

        # Extract text from each TextBlock and combine into a single string
        test_cases = "\n".join(block.text for block in response.content if hasattr(block, "text"))
        
        if not test_cases.strip():
            raise ValueError("Generated test cases are empty.")
        
        print("Generated test cases:", test_cases)
        return test_cases
    except Exception as e:
        print(f"An error occurred during test case generation: {e}")
        raise



def run_command(command: str) -> str:
    """
    Run a CLI command and return its output.
    """
    try:
        result = subprocess.run(
            command, shell=True, text=True, capture_output=True, check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.strip()}"


def validate_code(client, python_file: str, js_file: str) -> bool:
    """
    Validate converted JavaScript code against the original Python code.
    """
    # Generate test cases using LLM
    try:
        print("Generating test cases...")
        test_cases = generate_test_cases(client, python_file)
        print(f"Generated test cases: {test_cases}")
    except ValueError as e:
        print(f"Error during test case generation: {e}")
        return False

    # Parse test cases into a list
    test_cases_list = test_cases.split("\n\n")  # Basic splitting; refine as needed
    python_results = {}
    js_results = {}

    # Execute each test case
    for test_case in test_cases_list:
        print(f"Processing test case: {test_case}")
        # Simulate running the Python code
        python_command = f"python {python_file}"  # Modify to include test case inputs if needed
        python_results[test_case] = run_command(python_command)

        # Simulate running the JavaScript code
        js_command = f"node {js_file}"  # Modify to include test case inputs if needed
        js_results[test_case] = run_command(js_command)

    # Compare results
    validation_success = True
    for test_case in test_cases_list:
        if python_results[test_case] != js_results[test_case]:
            print(f"Mismatch for test case '{test_case}':")
            print(f"Python output: {python_results[test_case]}")
            print(f"JavaScript output: {js_results[test_case]}")
            validation_success = False

    # Display final validation results
    if validation_success:
        print("Validation successful: Python and JavaScript outputs match for all test cases.")
    else:
        print("Validation failed: There are mismatches between Python and JavaScript outputs.")

    return validation_success


if __name__ == "__main__":
    import sys
    from dotenv import load_dotenv

    load_dotenv()

    if len(sys.argv) != 3:
        print("Usage: python validation.py <python_file_path> <js_file_path>")
        sys.exit(1)

    python_file = sys.argv[1]
    js_file = sys.argv[2]
    env_path = os.path.join(os.getcwd(), '.env.example')
    load_dotenv(dotenv_path=env_path)

    # Create the Anthropic client
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: Missing ANTHROPIC_API_KEY in environment variables.")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    # Validate the files
    validate_code(client, python_file, js_file)
