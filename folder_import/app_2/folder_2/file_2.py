from os import pardir
from posixpath import dirname
import sys
from os.path import abspath, join

sys.path.append(abspath(join("app_1", "folder_1")))
print(sys.path)


from file_1 import First

f = First()
f.first()