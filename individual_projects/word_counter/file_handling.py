#BH 2nd file_handling.py
def ensure_file_exists(file_path):
    try:
        with open(file_path, "r") as f:
            pass
    except FileNotFoundError:
        with open(file_path, "w") as f:
            f.write("")
#Function to update document info
def update_document_info(file_path, word_count, timestamp):
    ensure_file_exists(file_path)
    with open(file_path, "a") as f:
        f.write(f"\n\nWord Count: {word_count}\nLast Updated: {timestamp}")
#Function view document
def get_user_content(file_path):
    ensure_file_exists(file_path)
    with open(file_path, "r") as f:
        content = f.read()
        user_content = content.split("Word Count:")[0].strip()
        return user_content
#Function to add content to document
def add_content_to_document(file_path, new_content):
    ensure_file_exists
    with open(file_path, "a") as f:
        f.write(new_content)