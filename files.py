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
# create new file
# print(os.makedirs('C:\\Users\\Asus\\Desktop\\Python\\Python-Bootcamp\\file'))

# reading from file and writing into file

hello  = open("C:\\Users\\Asus\\Desktop\\Python\\Python-Bootcamp\\new.txt")
print(hello.read())
hello.close()
hello  = open("C:\\Users\\Asus\\Desktop\\Python\\Python-Bootcamp\\new.txt")
content = hello.read()
print(content)
hello.close()
hello  = open("C:\\Users\\Asus\\Desktop\\Python\\Python-Bootcamp\\new.txt")

print(hello.readlines())
hello.close()
# w for write mode and
# a for append mode
hello  = open("C:\\Users\\Asus\\Desktop\\Python\\Python-Bootcamp\\new2.txt", 'w')
hello.write('heloooooooooo!!!!!!!!!')

hello.write('heloooooooooo!!!!!!!!!')

hello.close()

bacon  = open("becon.txt", 'w')

bacon.write('Bacon is not a vegetable.')
bacon.close()

bacon  = open("becon.txt", 'a')
bacon.write('Bacon is delicious')
bacon.close()

# shelve

import shelve
shefFile = shelve.open('mydata')
shefFile['cats'] = ['zophie', 'pooka','simon', 'Fat-hill', 'Cleo']
shefFile.close()

shefFile = shelve.open('mydata')
print(shefFile['cats'])
shefFile.close()

shefFile = shelve.open('mydata')

print(list(shefFile.keys()))
print(list(shefFile.values()))
shefFile.close()

import shutil
#shutil.copy("C:\\Users\\Asus\\Desktop\\Python\\Python-Bootcamp\\new2.txt", "C:\\Users\\Asus\\Desktop\\Python\\Python-Bootcamp\\file\\new2.txt")

# remove empty directory
# os.rmdir("C:\\Users\\Asus\\Desktop\\Python\\Python-Bootcamp\\file")

# remove folder and all of it's content
#shutil.rmtree("C:\\Users\\Asus\\Desktop\\Python\\Python-Bootcamp\\file")

import send2trash

send2trash.send2trash("C:\\Users\\Asus\\Desktop\\Python\\Python-Bootcamp\\new2.txt")

