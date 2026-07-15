import shutil
import os
from datetime import date


source_folder= r"C:\COA"

backup_root= r"C:\COA"


timestamp=date.today()
zip_name= os.path.join(backup_root, f"COA_backup_{timestamp}")



try:

    shutil.copytree(source_folder, destination)
    print(f"Folder backup created: {destination}")

except Exception as e:
    print(F"Error: {e}")
