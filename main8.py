valid_formats = [
    "docx",
    "pdf",
    "txt",
    "pptx",
    "ppt",
    "md",
]

# Don't edit above this line

# Complete the function to pair document names with their formats
# and filter out invalid formats
# Each document name should be paired with its corresponding format
# Return a list of tuples containing only valid document-format pairs
def pair_document_with_format(doc_names, doc_formats):
    zipped = list(zip(doc_names, doc_formats))
    return list(filter(lambda invalid: invalid[1] in valid_formats, zipped))