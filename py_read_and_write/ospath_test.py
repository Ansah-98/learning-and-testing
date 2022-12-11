import os 
import shelve 

#creating a directory with os.mkdir module(""  path in as a parameter)
os.mkdir('/Users/mac/learn_techniques/py_read_and_write/first.py')

#creating a path for any os with the os.path.join function( takes multiple argunments seperated with commas)
os.path.join('.')
# it combines all the parameters passed and forms a path with depending on the os 


#calling os.path.abspath(path)  converts the path provided to an absolute path
#the absolute path always begins with the root directory
os.path.abspath('./scripts')


#returns true if path provided is absolute directory
os.path.isabs()

#provides a relative path from the starting parameter to the path value ,if the start parameter isnt provided then the working directory is used
# takes two argument start and path ,
os.path.relpath()

#calling os.path.dirname(path) returns everything that comes before the path lash slash
os.path.dirname()


#calling os.path.basename(path) returns everything that comes after the lash slash of the path argument 
os.path.basename()

#calling os.path.split(path) returns both the dirname and the basename of the path in a tuple
os.path.split()

#FINDING FILE SIZES AND LIST OF FOLDER CONTENTS 

#os.path.getize() will return the the size of the file in that directory
os.path.getsize()

#os.listdir is in the os module it returns the files in a particular directory
