import os

base_path= "/e2open/home/dgond@prod.e2open.com/Dipak"

os.makedirs(os.path.join(base_path, "deploy", "MOUNT"), exist_ok=True)

MOUNT_subdirs =["Logs","Backup", "config",]


for subdir in MOUNT_subdirs:

    os.makedirs(os.path.join(base_path, "MOUNT", subdir),exist_ok=True)


print("Directory sturcture are created"
