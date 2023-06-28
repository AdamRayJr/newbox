#########################################
# Author: Adam Ray Jr
# Date: 2023-06-28
# Github: https://github.com/AdamRayJr/
#########################################

#!/bin/bash

create_directory() {
    if [ -d "$1" ]; then
        echo "Directory '$1' already exists."
    else
        mkdir -p "$1"
        echo "Directory '$1' created successfully."
    fi
}

create_file() {
    if [ -f "$1" ]; then
        echo "File '$1' already exists."
    else
        touch "$1"
        echo "File '$1' created successfully."
    fi
}

# Prompt user for IP address to export
read -p "Enter the IP address (e.g. 192.168.x.x): " ip

# Export IP as an environment variable
export IP="$ip"

echo -e "\nEnvironment variables exported:"
echo "export IP=\"$ip\""

# Prompt user for base directory name
read -p "Enter the base directory name: " base_directory

create_directory "$base_directory"

directories=("vulns" "files")  # Specify the directories to create
files=("passwords" "users" "hashes")  # Specify the files to create

for directory_name in "${directories[@]}"; do
    directory_path="$base_directory/$directory_name"
    create_directory "$directory_path"
done

for file_name in "${files[@]}"; do
    file_path="$base_directory/$file_name"
    create_file "$file_path"
echo "suckit"
done
