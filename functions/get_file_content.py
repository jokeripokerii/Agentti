import os
from google import genai
from google.genai import types
from functions.config import *

def get_file_content(working_directory, file_path):
    try:
        #Setting up and checking filepaths
        absolute_path = os.path.abspath(working_directory)
        absolute_filepath = os.path.abspath(file_path)
        target_file = os.path.normpath(os.path.join(absolute_path, file_path))

        #Checks if the target file is within allowed limits
        valid_target_dir = os.path.commonpath([absolute_path, target_file]) == absolute_path

        #Checks if targer is a file
        if os.path.isfile(target_file) == False:
            return f'Error: File not found or is not a regular file: "{file_path}"'

        #Checks if target is within allowed limits
        if valid_target_dir == False:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        #Read file contents
        with open(target_file) as t:
            content = t.read(MAX_CHARS)
            # After reading the first MAX_CHARS...
            if t.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'


        return content
    except Exception as e:
        return f"Error: {e}"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Lists file content in a specified file relative to the working directory, providing contents of the file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to read contents from, relative to the working directory.",
            ),
        },
    ),
)