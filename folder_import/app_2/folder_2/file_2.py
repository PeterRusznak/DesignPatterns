import sys
from os.path import abspath

elso_dir = abspath( "app_1"+ '/folder_1/')
sys.path.append(elso_dir)

from file_1 import First


f = First()
f.first()