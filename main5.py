# Remove lines that start with a hyphen from the document
# Each line in the document is separated by a newline character.
# Return the cleaned document as a single string.
# Use the filter function and a lambda expression to accomplish this.
def remove_invalid_lines(document):
    return "\n".join(
        filter(lambda line: not line.startswith("-"), document.split("\n"))
    )