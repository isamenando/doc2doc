# So inside your loop:
# Instead of doing something once per tuple, you need to do something once per extension in the tuple’s list.
# Questions to guide you:
# How can you change your for loop so that you can access both the file type and the list of extensions by name, instead of indexing with file[0] and file[1]?
# Once you have file_type and extensions, how could you add another loop inside that goes through each ext in extensions and adds an entry to file_extension_dict?
# Nested loops are a common pattern when dealing with iterating through lists of lists or list of touples.
def file_type_getter(file_extension_tuples):
    file_extension_dict = {}
    for file_type, extensions in file_extension_tuples:
        for ext in extensions:
            # Add an entry to the dictionary for each extension
            file_extension_dict[ext] = file_type
    # Return a lambda function that accepts a string (a file extension) and returns its file type from the dictionary.
    #Use the .get dictionary method in the lambda function to return the file type of the extension if found or "Unknown" if it's missing.
    return lambda ext: file_extension_dict.get(ext, "Unknown")
