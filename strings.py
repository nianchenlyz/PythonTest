# strings.py

# Truncating long strings

long_string = "loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooongssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssstring"
string_after_trimming = long_string[:97] + '...' if len(long_string) > 97 else long_string
# result 'loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo...'

# shorter way
long_string = "loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooongssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssstring"
string_after_trimming = long_string[:97] + (long_string[97:] and '...')
# result 'loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo...'

