import shelve


#the shelve method allows you to save variables to binary shelf files using the shelf module
#this your programs can restore data to variables from the hard drives.
shelf_file = shelve.open('mydata')
cats = ['cats','zoophie','money']
print(shelf_file['cats'])
shelf_file.close