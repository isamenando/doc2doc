# Change bullet style from '-' to '*'
# The function takes a document as a string,
# where each line may start with a bullet '-'.
# It converts all bullets from '-' to '*'
# and returns the modified document as a string.
def change_bullet_style(document):
    lines_list = document.split("\n")
    change_bullets = map(convert_line, lines_list)
    rejoined_doc = "\n".join(change_bullets)
    return rejoined_doc


# Don't edit below this line

# Helper function
# Converts a single line's bullet style
# from '-' to '*'
def convert_line(line):
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line