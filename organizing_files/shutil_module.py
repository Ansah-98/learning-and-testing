#COPYING FILES WE USE THE SHUTIL MODULE

#also known as the shell utilities
#used to copy , move ,rename and delete a files in your python program
import send2trash as s2t
import shutil , os ,zipfile

starting = os.getcwd()
starting = (starting +'/organizing_files/mee.txt' )
destination = os.getcwd()
print(destination)
shutil.copy( starting, '/Users/mac/Desktop/c_learn')


#shutil.copytree(source destination ) copies entire folder and files in them to the destination
shutil.copytree()


#MOVING (CUTTING) AND RENAMING FILES AND FOLDERS
shutil.move(starting ,destination)

#deleting files and folders from location
os.unlink()
#os.unlink is used to remove a file from a path specified as parameter 

os.rmdir()
#its used to delete folder from the path specified 

shutil.rmtree
#used to delete a folder and all it content files and folders 

#this module is used to safely delete files to trash or recycle bin
s2t.send2trash()

#the zipfile module is used to extract compressed files and give info about compressed files
emptyfile = zipfile.ZipFile()

#first need to create an instance of zipfile and use the method of that instance to access the the zip folder interested 
#methods include ,extractall(), extract(), namelist(), getinfo()
