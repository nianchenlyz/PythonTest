import os
""" Useful information in documentation
    https://docs.python.org/2/library/os.path.html

"""

base_path = os.path.abspath('.')  # C:\\Users\\User_name or /home/user_name

relative_path = os.path.relpath('.')  # relative path '.'

os.path.join('path', 'to', 'test', 'folder')  # path\\to\\test\\folder or path/to/test/folder
