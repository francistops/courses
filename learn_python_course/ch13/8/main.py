# don't use .join() method
def join_strings(strings):
    joined_str = ''
    for word in strings:
        if word == strings[-1]:
            joined_str += word
        else:
            joined_str += word + ','
    return joined_str
