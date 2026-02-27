import os
from google import genai
from google.genai import types
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        #Setting up and checking filepaths
        absolute_path = os.path.abspath(working_directory)
        absolute_filepath = os.path.abspath(file_path)
        target_file = os.path.normpath(os.path.join(absolute_path, file_path))

        #Checks if the target file is within allowed limits
        valid_target_dir = os.path.commonpath([absolute_path, target_file]) == absolute_path
       
        #Checks if target is within allowed limits
        if valid_target_dir == False:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        #Checks if targer is a file
        if os.path.isfile(target_file) == False:
            return f'Error: "{file_path}" does not exist or is not a regular file'

        #Running wanted file
        command = ["python", target_file]
        if args != None:
            command.extend(args)
        running_command = subprocess.run(command, capture_output=True, text=True, timeout=30)

        if file_path[-3:] != ".py":
            return f'Error: "{file_path}" is not a Python file'


        #Constructs string for returning
        outputstring = []
        if running_command.returncode != 0:
            outputstring.append("Process exited with code {running_command.returncode}")
        if len(running_command.stdout) < 1 and len(running_command.stderr) < 1:
            outputstring.append("No output produced")
        else:
            outputstring.append(f"STDOUT: {running_command.stdout}")
            outputstring.append(f"STDERR: {running_command.stderr}")

        return "\n".join(outputstring)
    except Exception as e:
        return f"Error: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs the Python file specified in the filepath",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to run the file from, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Optional command-line arguments passed to the Python file.",
                items=types.Schema(type=types.Type.STRING),
            ),
        },
    ),
)
