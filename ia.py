import os
import sys

from openai import OpenAI


def get_current_code():
    # Read the current source code of this script
    with open(__file__, 'r') as f:
        return f.read()


def fetch_updated_code_from_openai(current_code):
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that updates Python code."},
            {
                "role": "user",
                "content": f"Here is the current code:\n\n{current_code}\n\nPlease update and improve this code."
            }
        ]
    )

    return completion.choices[0].message['content']


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

    print("Getting updated code from OpenAI...")
    new_code = fetch_updated_code_from_openai(current_code)

    print("Updating the script with the new code...")
    update_code(new_code)

    print("Restarting the updated script...")
    restart_program()

    print("This line will never be executed because the process is replaced.")
