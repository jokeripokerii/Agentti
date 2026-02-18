import os

def get_files_info(working_directory, directory="."):
    try:      
        #Checks filepaths so AI can only access specified things
        absolute_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(absolute_path, directory))
        valid_target_dir = os.path.commonpath([absolute_path, target_dir]) == absolute_path

        #Checks that the target is actually a directory
        if os.path.isdir(target_dir) == False:
            return f'Error: "{directory}" is not a directory'

        #Checks if target is within allowed limits
        if valid_target_dir == False:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        #Creates a list of items in the directory
        dir_items = []
        for i in os.listdir(target_dir):
            filu_koko = os.path.getsize(target_dir+"/"+i)
            onko_hakemisto = os.path.isdir(target_dir+"/"+i)
            dir_items.append(f"- {i}: file_size={filu_koko} bytes, is_dir={onko_hakemisto}")
            
        #print("\n".join(dir_items))
        return "\n".join(dir_items)
    except Exception as e:
        print(f"Error: {e}")
