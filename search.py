import os

def search_in_files(root_dir, search_text):
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        for i, line in enumerate(f, 1):
                            if search_text in line:
                                print(f"Found in {file_path}: Line {i}: {line.strip()}")
                except UnicodeDecodeError:
                    # Retry with a different encoding if utf-8 fails
                    try:
                        with open(file_path, 'r', encoding='ISO-8859-1') as f:
                            for i, line in enumerate(f, 1):
                                if search_text in line:
                                    print(f"Found in {file_path}: Line {i}: {line.strip()}")
                    except Exception as e:
                        print(f"Could not read file {file_path}: {e}")

# Set your project directory and the text to search
search_in_files(".", "HuggingFaceEmbeddings")
