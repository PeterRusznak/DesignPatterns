import os,sys
# os.path.join(os.path.curdir, 'file.name')
sys.path.append("/home/pr/gyak/DesignPatterns/folder_import/app_1/folder_1")
# print(sys.path)

from file_1 import First

f = First()
f.first()