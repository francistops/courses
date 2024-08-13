def reverse_string(s):
    # return s[::-1]
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]
