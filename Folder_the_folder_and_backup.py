import shutil
import os
from datetime import date


source_folder= "/e2open/home/dgond@prod.e2open.com/Dipak"

backup_root= "/e2open/home/dgond@prod.e2open.com"


timestamp=date.today()
destination= os.path.join(backup_root, f"Dipak_backup_{timestamp}")



try:

    shutil.make_archive(destination, 'zip', source_folder)
    print(f"Folder backup created: {destination}.zip")

except Exception as e:
    print(F"Error: {e}")
