#########################################
# Author: Adam Ray Jr
# Date: 2023-06-28
# Tested with Python v3
# Github: https://github.com/AdamRayJr/
#########################################

import os

def create_directory(directory_name):
    if os.path.exists(directory_name):
        print(f"Directory '{directory_name}' already exists.\nQuitting...")
        exit()
    else:
        os.makedirs(directory_name)
        print(f"Directory '{directory_name}' created successfully.")

def create_file(file_name):
    if os.path.exists(file_name):
        print(f"File '{file_name}' already exists.\nQuitting...")
        exit()
    else:
        with open(file_name, 'w') as file:
            file.write('')
        print(f"File '{file_name}' created successfully.")

# Prompt user for IP address to export
ip = input("\nEnter the IP address (e.g. 192.168.x.x): ")

# Export IP as an environment variable
os.environ["IP"] = ip
export_ip_cmd = f'export IP="{ip}"'

print("\nEnvironment variables exported:")
print(export_ip_cmd)

# Prompt user for base directory name
base_directory = input("\nEnter the base directory name: ")

create_directory(base_directory)

directories = ['vulns', 'files']  # Specify the directories to create
files = ['passwords', 'users', 'hashes']  # Specify the files to create

for directory_name in directories:
    directory_path = os.path.join(base_directory, directory_name)
    create_directory(directory_path)

for file_name in files:
    file_path = os.path.join(base_directory, file_name)
    create_file(file_path)
