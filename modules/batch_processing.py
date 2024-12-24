import time
import os

async def process_batch_results(client, batch_id, path_js_project, python_files):
    """
    Process batch based on ID and writes results into JS files.
    """
    print(f"Processing batch results for batch ID: {batch_id}")

    while True:
        batch_status = client.messages.batches.retrieve(batch_id)
        if batch_status.processing_status == "ended":
            print(f"Batch {batch_id} has completed processing.")
            break
        elif batch_status.processing_status == "failed":
            raise RuntimeError(f"Batch {batch_id} processing failed.")
        print(f"Batch {batch_id} is still processing...")
        time.sleep(3)

    results = client.messages.batches.results(batch_id)
    if not results:
        raise ValueError("No results returned for the batch.")

    for result in results:
        custom_id = result.custom_id
        matching_file = next((f for f in python_files if os.path.splitext(f)[0] == custom_id), None)
        if not matching_file:
            print(f"No matching Python file found for custom ID: {custom_id}")
            continue

        if result.result.type == "succeeded":
            converted_code_blocks = result.result.message.content
            converted_code = "".join(block.text for block in converted_code_blocks)
            js_file_name = os.path.splitext(matching_file)[0] + ".js"
            js_output_path = os.path.join(path_js_project, js_file_name)

            # Ensure the directory exists
            os.makedirs(os.path.dirname(js_output_path), exist_ok=True)

            with open(js_output_path, "w") as js_file:
                js_file.write(converted_code)

            print(f"JavaScript code written to {js_output_path}")
        else:
            print(f"Error processing result for custom ID {custom_id}")

    print("Batch processing complete.")
    return True
