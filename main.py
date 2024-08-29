import os
import sys


def restart_program():
    print("Restarting the program...")
    os.execv(sys.executable, ['python'] + sys.argv)


if __name__ == "__main__":
    print("This program will restart itself.")
    restart_program()
    print("This line will never be executed because the process is replaced.")
