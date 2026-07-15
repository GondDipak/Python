print(file.readline())
file = open (r"C:\COA\Dipak\Spider.txt")

print(file.read())

file.close()
________________________________________________________________

'with open(r"C:\COA\Dipak\Spider.txt") as file:
 #  print(file.readline())

file.close()'
___________________________________________________________________
Iterating through files--------------


with open() as file: # to conver upper and lower case

    for line in file:
        print(line.lower())

with open(r"C:\COA\Dipak\Spider.txt") as file: #used strip() to extra gap from one to a new line
#   for line in file:
 #      print(line.strip().upper())
_________________________________________________________________________________
import os
source_path=(r"C:\COA\Dipak\Dipak_g")
os.mkdir(source_path)
with open(r"C:\COA\Dipak\Dipak_g\Spider.txt", "w") as file: # this will open new file and write
   file.write("my name is dipak \nMy name is Chiku")


with open("C:\COA\Dipak\Spider.txt", "a") as file: #'a' will open the file and add the text
 #  file.write("\nMy name is yahvi")
________________________________________________________________________

#FILE PATH------------
#Relative path
#Absolute path - fill path of file

#Working with files-----------------------------------

#import os
#source_path=(r"C:\COA\Dipak\spider.txt")
#new_file=(r"C:\COA\Dipak\spider_new.txt")
#os.rename(source_path, new_file)
#print("file Renamed")

#import os
#os.remove(r"C:\COA\Dipak\spider_new.txt")
#print("file removed")

#import os
#os.path.exists(r"C:\COA\Dipak\spider_new.txt")

#import os
#source_path= (r"C:\COA\Dipak\Spider.txt")
#size= os.path.getsize(source_path)
#time= os.path.getmtime(source_path)
#print(size
#print(time)


#import os
#import datetime
#source_path= (r"C:\COA\Dipak\Spider.txt")
#timestamp= os.path.getmtime(source_path)
#datetime.datetime.fromtimestamp(timestamp)
#print(datetime.datetime.formattimestamp(timestamp))

import os
dir = r"C:\COA\Dipak"
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))

import os
def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename, "w") as file:
    file.write(comments)
  filesize = os.path.getsize(filename)
  return(filesize)

print(create_python_script("program.py"))


import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open(filename, "w")as file:
    file.write("my name is Dipak")

  timestamp = os.path.getmtime(filename)
  # Convert the timestamp into a readable format, then into a string
  datetime.datetime.fromtimestamp(timestamp)
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return (datetime.datetime.fromtimestamp(timestamp))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-d


import os

def new_directory(directory, filename):
 
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
    os.mkdir(directory)
    
  # Create the new file inside of the new directory
  os.chdir(directory)
  with open (filename, "w") as file:
    pass

  # Return the list of files in the new directory
  return filename

print(new_directory("PythonPrograms", "script.py"))

                     
                     








