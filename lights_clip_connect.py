import subprocess
import sys

def select_clip(arg1, arg2):
    cmd = f'curl -X POST "http://10.11.250.225:8080/api/v1/composition/layers/{arg1}/clips/{arg2}/connect" -v'
    subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Error: Invalid number of arguments. 2 integers expected: row column.")
        sys.exit()
    try:
        arg1 = int(sys.argv[1])
        arg2 = int(sys.argv[2])
    except ValueError:
        print("Error: Arguments should be integers (row column).")
        sys.exit()
    select_clip(arg1, arg2)
