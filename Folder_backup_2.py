import shutil
import os
from datetime import date


source_folder = r"C:\COA\Dipak"
backup_root= r"C:\COA\Dipak"



timestamp=date.today()

destination= os.path.join(backup_root,f"Dipak_Backup_{timestamp}" )


try:

    shutil.copytree(source_folder, destination)

    print(f"folder backup create: {destination}")


except Exception as e:

    print(f"Error: {e}")

