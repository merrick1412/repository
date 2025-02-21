#!/bin/sh
# Author: Merrick Moncure
# Assignment: Write a shell script to move a file or directory to a .junk directory
# Purpose: This script moves a specified file or directory to a hidden .junk directory in the user's $HOME folder,
# ensuring error handling and interactive user input for specific conditions.

# Check if exactly one argument is provided
if [ "$#" -ne 1 ]; then
  echo "Error: Exactly one argument is required."
  exit 1
fi

FILENAME="$1"
JUNK_DIR="$HOME/.junk"

# Check if the file exists in the current directory
if [ ! -e "$FILENAME" ]; then
  echo "Error: The file or directory '$FILENAME' does not exist."
  exit 1
fi

# Check if the file is writable
if [ ! -w "$FILENAME" ]; then
  echo "Error: The file or directory '$FILENAME' is not writable."
  exit 1
fi

# Handle if the file is a directory
if [ -d "$FILENAME" ]; then
  echo "'$FILENAME' is a directory. Do you want to junk the entire directory? (y/n)"
  read -r CONFIRM
  if [ "$CONFIRM" != "y" ]; then
    echo "The directory will not be junked."
    exit 0
  fi
fi

# Create the .junk directory if it doesn't exist
if [ ! -d "$JUNK_DIR" ]; then
  mkdir "$JUNK_DIR"
  if [ "$?" -ne 0 ]; then
    echo "Error: Failed to create .junk directory."
    exit 1
  fi
fi

# Handle if the file already exists in the .junk directory
if [ -e "$JUNK_DIR/$FILENAME" ]; then
  if [ -d "$FILENAME" ]; then
    echo "Error: A directory with the same name already exists in the .junk directory."
    exit 1
  fi

  echo "A file with the same name already exists in the .junk directory. Overwrite it? (y/n)"
  read -r CONFIRM
  if [ "$CONFIRM" != "y" ]; then
    echo "The file will not be junked."
    exit 0
  fi
fi

# Move the file to the .junk directory
mv "$FILENAME" "$JUNK_DIR/"
if [ "$?" -eq 0 ]; then
  echo "'$FILENAME' has been successfully moved to the .junk directory."
  exit 0
else
  echo "Error: Failed to move '$FILENAME' to the .junk directory."
  exit 1
fi
