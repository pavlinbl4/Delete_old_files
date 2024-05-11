# Here's an example function in Python that deletes all files with a
# specific extension from a directory that are older than a specified number of days:


import os
from datetime import datetime

def delete_files_older_than(dir_path, extension, days):
    """
    Deletes all files with a specific extension from a directory that are older than a specified number of days.
    """
    # Get current date and time
    now = datetime.now()

    # Iterate over files in directory
    for filename in os.listdir(dir_path):
        # Check file extension
        if filename.endswith(extension):
            # Get file creation time
            file_path = os.path.join(dir_path, filename)
            file_creation_time = os.path.getctime(file_path)
            file_creation_date = datetime.fromtimestamp(file_creation_time)

            # Check if file is older than specified number of days
            delta = now - file_creation_date
            if delta.days > days:
                # Delete file
                os.remove(file_path)
if __name__ == '__main__':

    delete_files_older_than("/Volumes/big4photo/Downloads", "doc", 1) # Delete all .txt files older than 10 days
