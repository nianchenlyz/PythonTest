import os
import re
""" Useful information in documentation
    https://docs.python.org/2/library/os.path.html

"""

# Path

base_path = os.path.abspath('.')  # C:\\Users\\User_name or /home/user_name

relative_path = os.path.relpath('.')  # relative path '.'

os.path.join('path', 'to', 'test', 'folder')  # path\\to\\test\\folder or path/to/test/folder

# Miscellaneous 

os.listdir('.')

for dirname, dirnames, filenames in os.walk('.'):
    print dirname, filenames


# example of eliminating duplicates
# file like `file0001_20160222.xml`
previous_file_name = ''
for dirname, dirnames, filenames in os.walk('.'):
	filenames.sort()  # sorting files alphabetically
	try:
		for file_name in filenames:  # looping over all files in folder
			filename_search = re.search('^(file\d{4})_\d{8}.xml$', file_name)  # regex
			if filename_search and filename_search.group():  # when regex and group is not None
				# will be True if file has same beginning, but different date
				if filename_search.group(1) in previous_file_name:
					# do something, remove, move file to different folder with shutil
					continue  # temporary
			previous_file_name = file_name
	except Exception as e:
		print 'Error occurred with exception: {}'.format(e.message)

print 'All files checked'



