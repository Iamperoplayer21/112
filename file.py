import os
import shutil

source = "/C:\Users\Admin\Downloads"
destination = "/C:\Users\Admin\Desktop\New folder (7)"

list_of_files = os.listdir(source)
print(list_of_files)

for file in list_of_files:
    name, extensions = os.path.splitext(file)
    print(name)
    print(extensions)


    if extensions == '':
            continue
    if extensions in [ '.txt', '.doc', '.docx', '.pdf']:

        path1 = source + '/' + file
        path2 = destination + '/' + 'download images'
        path3 = destination + '/' + 'download images'+'/'+file

        if os.path.exists(path2):
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            shutil.move(path1, path3)