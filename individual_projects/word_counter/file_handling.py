#BH 2nd file_handling.py
#import sys and os
import sys
import os
#Function to view document
def get_content_parts(file_path):
    ensure_file_exists(file_path)
    try:
        with open(file_path, "r") as f:
            content = f.read()
    except Exception as e:
        sys.exit(f"An error occurred while reading the file: {file_path}")
    index_pos = content.find("Word Count:")
    user_content = content[:index_pos].strip() if index_pos != -1 else content.strip()
    document_info = content[index_pos:].strip() if index_pos != -1 else ""
    return { "user_content": user_content, "document_info": document_info }
#Function for ensuring file exists, if not create it
def ensure_file_exists(file_path):
    if not os.path.exists(file_path):
        try:
            with open(file_path, "w") as f:
                f.write("")
        except Exception as e:
            sys.exit(f"An error occurred while creating the file: {file_path}")
#Function to update document info
def update_document_info(file_path, word_count, timestamp):
    ensure_file_exists(file_path)
    try:
        with open(file_path, "a") as f:
            f.write(f"\n\nWord Count: {word_count}\nLast Updated: {timestamp}")
    except Exception as e:
        sys.exit(f"An error occurred while updating document info: {file_path}")
#Function to add content to document
def add_content_to_document(file_path, new_content):
    content_parts = get_content_parts(file_path)
    try:
        with open(file_path, "w") as f:
            if len(content_parts['user_content']) > 0:
                f.write(f"{content_parts['user_content']} ")
            f.write(new_content)
            if len(content_parts['document_info']) > 0:
                f.write(f"\n\n{content_parts['document_info']}")
    except Exception as e:
        sys.exit(f"An error occurred while adding content to the document: {file_path}")