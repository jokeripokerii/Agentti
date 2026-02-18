import os

def get_file_content(working_directory, file_path):
    try:
        absolute_path = os.path.abspath(working_directory)
        print(absolute_path)
        absolute_filepath = os.path.abspath(file_path)
        print(absolute_filepath)

        target_file = os.path.normpath(os.path.join(absolute_path, file_path))
        print(target_file)

        print(os.path.commonpath([absolute_path, target_file]))
        print(os.path.isfile(target_file))

        #Checks if targer is a file
        if os.path.isfile(target_file) == False:
            print("Testing error")
            return f'Error: File not found or is not a regular file: "{file_path}"'

        return "testi"
    except Exception as e:
        print(f"Error: {e}")

get_file_content("calculator", "pkg/render.py")