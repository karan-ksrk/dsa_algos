import os
import argparse

# Set up argument parsing
parser = argparse.ArgumentParser(description="Create a folder with specific files.")
parser.add_argument('-d', '--directory', required=True, help='The name of the folder to create')
args = parser.parse_args()

# Use the directory name from the command line argument
folder_name = args.directory

# Create the folder
os.makedirs(folder_name, exist_ok=True)

# Create the files with prewritten content
with open(os.path.join(folder_name, "output.txt"), "w") as f:
    pass

with open(os.path.join(folder_name, "input.txt"), "w") as f:
    pass

with open(os.path.join(folder_name, "main.py"), "w") as f:
    f.write(f"""\
import config
            

def {folder_name}():
    pass

if __name__ == '__main__':
    #arr = list(map(int, input().split()))
    {folder_name}()
""")
with open(os.path.join(folder_name, "config.py"), "w") as f:
    f.write("""\
import sys
import heapq
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
""")