path = r'c:\user\eggs.png'
path = 'c:\\user\\eggs.png'
print(path)

import os
path = os.path.join('folder1','folder2', 'folder3')
print(path)

# current working directory
print(os.getcwd())

# absolute file path and relative file path

# absolute file start with root file path

# relative file path current working file

# single dots(.) stands for this directory or this folder

# double dots(..) stands for parent folder

# exists or isfile isdir
print(os.path.exists('c:\\users'))

# size

print(os.path.getsize('c:\\windows'))

# os.listdir('c:\\')

print(os.makedirs('C:\\Users\\Asus\\Desktop\\Python\\Python-Bootcamp\\file'))





