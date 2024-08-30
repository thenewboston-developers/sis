import os
import sys

from promptlayer import PromptLayer


def get_current_code():
    # Read the current source code of this script
    with open(__file__, 'r') as f:
        return f.read()


def fetch_updated_code(current_code):
    promptlayer_client = PromptLayer()
    response = promptlayer_client.run(
        prompt_name="sis",
        input_variables={
            "current_code": current_code
        }
    )
    return response["prompt_blueprint"]["prompt_template"]["messages"][-1]["content"][0]["text"]


def update_code(new_code):
    # Overwrite the current file with the new code
    with open(__file__, 'w') as f:
        f.write(new_code)


def restart_program():
    print("Restarting the program...")
    os.execv(sys.executable, ['python'] + sys.argv)


if __name__ == "__main__":
    print("Fetching the current source code...")
    current_code = get_current_code()

    print("Getting updated code...")
    new_code = fetch_updated_code(current_code)

    print("Updating the script with the new code...")
    update_code(new_code)

    print("Restarting the updated script...")
    restart_program()

    print("This line will never be executed because the process is replaced.")
