from os import pardir
from posixpath import dirname
import sys
from os.path import abspath, join

x = join("app_1", "folder_1")
elso_dir = abspath(x)
sys.path.append(elso_dir)

from file_1 import First

f = First()
f.first()