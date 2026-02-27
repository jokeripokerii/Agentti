import os
from google import genai
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        #Setting up and checking filepaths
        absolute_path = os.path.abspath(working_directory)
        absolute_filepath = os.path.abspath(file_path)
        target_file = os.path.normpath(os.path.join(absolute_path, file_path))

        #Checks if the target file is within allowed limits
        valid_target_dir = os.path.commonpath([absolute_path, target_file]) == absolute_path

        #Checks that the target is actually a directory
        if os.path.isdir(target_file) == True:
            print("Isdir error checker")
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        #Checks if target is within allowed limits
        if valid_target_dir == False:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        #Checks and creates parent directories
        os.makedirs(os.path.dirname(target_file), exist_ok=True)

        #Writes contents to the file it creates
        with open(target_file, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes in a specified file that is in a directory relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path", "content"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="This is the content that will be written to the specified file",
            ),
        },
    ),
)
