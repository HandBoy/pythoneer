"""
The reason for this is that when you use join, Python allocates
memory for the joined string only one time, but when you concatenate
strings, Python has to allocate new memory for each concatenation
because the Python string is immutable.

"""
first_name = "Json"
last_name = "smart"

# Not a recommended way to concatenate string
full_name = first_name + "  " + last_name

# More performant and improve readability
print(" ".join([first_name, last_name]))