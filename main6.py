import functools

# Joins two sentences with a period and a space.
def join(doc_so_far, sentence):
    return doc_so_far + ". " + sentence

# Joins the first n sentences from a list into a single string.
# If n is 0, returns an empty string.
# Adds a period at the end of the final string.
def join_first_sentences(sentences, n):
    if n == 0:
        return ""
    return functools.reduce(join, sentences[:n]) + "."