import os

dir= r"C:\COA\Dipak"

for name in os.listdir(dir):

    fullname= os.path.join(dir, name)

    if os.path.isdir(fullname):

        print(f"{fullname} is a directory")

    else:
        print(f"{fullname} is a file")
