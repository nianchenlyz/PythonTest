"""Examples of functions from os library

"""

file_name = 'document.pdf'

# fn stands for file name without extension
# splitext helps getting extension and rest of the file name
fn, extension = os.path.splitext(file_name)

