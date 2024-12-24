## Setup project

- Make sure you have Python 3.12+ installed
- install poetry: `pip install poetry`
- initialize env and install dependencies: `POETRY_VIRTUALENVS_IN_PROJECT=1 poetry install --no-root`
- activate the virtual environment: `poetry shell`

## In case you add js dependencies

- install node in the machine and run `npm install` in this project.

### how to install dependency

After doing the above and having `poetry shell` activited, you can use `poetry add PACKAGE_NAME`

### How to run the command locally

After doing the above and having `poetry shell` activited, you can use `python ./convert.py basic_calculator`

## What is needed? what is this task?

We need you to implment a tool that converts python projects into js projects. You will utalize LLMs to achive this task.
As part of the assignment, you will be provided with an OpenAI or an Anthropic API keys. You can utalize these APIs to build this tool.

After you follow up the setup instructions, you can use `python ./convert.py basic_calculator` (or any test name - basic_calculator is a test name that reflects a folder inside the tests folder) as an entry point to your code.

What you need to convert is a python project that is located in a `py` folder inside the `tests` folder. The tool above takes a test case name.
What you need to do is take the test name and run a LLM-Powered logic that can conver this to a correctly working js project that you should locate in the folder `js` next to the `py` folder.

For the test `basic_calculator` you have the output also already created in the `js` folder.

Here are the cases you need to think about and consider:

- the project can have multiple files.
- Support only 1 entry file (cli.py, cli.js when converted).
- The code in the project can be a cli tool that you can call with arugments, or cli tool that you just run (no arugments)
- In terms of dependecies, you should focus on cases where there are no dependeices.
- We have created 3 test cases for you, you can add more as you see fit. Please include these cases in the PR you send.
- We will evaulate your assignment based on:
  -- Fully working or not?
  -- Code running on cases in the code? we will add more cases to test on.
  -- Code quality.
  -- Promot quality.

Tips for logic and how to use LLMs:

- You should consider utalizing function/tool calling that LLMs provide.
- You can build this as 1 agent with multiple tool and make the CLI a simple call to the LLM with a loop.
- You can build this as a pipeline that can utilize LLMs for part of it and then some stuff can be staticly build.
- As part of the the conversion, we expect your tool to run the python code and the generated js code. If the tool has arugments, we expect you to use LLMs to generate test cases and then run them on python and then rerun them on the converted js code to validate.

Libraries to use to build the tool: feel free to use any libraries/framework you need to build this tool - the code needs to fully run locally, the only external depdency you can have (as a service) is openai LLMs or anthropic LLMs.

# UPDATES:

#### How to run the basic project?

py convert.py folder_name_inside_tests_folder
**Ex: **py convert.py print_pattern

#### Why batching?

Although using basic requests with a basic delay in a loop is faster to generate results, you may run into limits (ex: too many requests, tokens , etc) - If the amount of files is large, it will either take more time or fail before the batch solution.

#### How to use Validation?

py modules/validation.py tests/folder/py/python_file.py tests/folder/js/js_file.js

**Validation **may result in a false positive, and although you can write successful automated cases, much like real QA it's best to have someone check it for various codes.

