from os import pardir
from posixpath import dirname
import sys
from os.path import abspath, join

sys.path.append(join("app_1", "folder_1"))

from file_1 import First

f = First()
f.first()