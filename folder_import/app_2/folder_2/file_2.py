
import sys
from os.path import abspath, join

print("ABSPATH = ", abspath("."))

#if called for folder_2
sys.path.append(abspath(join("..","..","app_1", "folder_1")))

#if called from root folder /usr/bin/python3 app_2/folder_2/file_2.py
sys.path.append(abspath(join("app_1", "folder_1")))
print(sys.path)


from file_1 import First

f = First()
f.first()