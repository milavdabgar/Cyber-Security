import os

def create_folders_infinite(base_path='./'):
    """
    Create folders infinitely in the specified base path.

    Parameters:
    - base_path: Base path where folders will be created. Defaults to current directory './'.
    """
    folder_index = 1
    while True:
        folder_name = f"Folder{folder_index}"
        folder_path = os.path.join(base_path, folder_name)
        os.makedirs(folder_path)
        print(f"Folder '{folder_name}' created successfully at '{folder_path}'.")       
        folder_index += 1


create_folders_infinite()
