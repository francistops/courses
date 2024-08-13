def find_longest_word(document, longest_word=""):
    #    longest_count = float('-inf')
    #    for word in document:
    #        if len(word) > longest_count:
    #            longest_word = word
    #    return longest_word

    if not document:
        return longest_word

    words = document.split(maxsplit=1)
    if words:
        current_word = words[0]

        if len(current_word) > len(longest_word):
            longest_word = current_word

        if len(words) > 1:
            return find_longest_word(words[1], longest_word)

    return longest_word
