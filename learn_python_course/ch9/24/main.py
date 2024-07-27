def filter_messages(messages):
    f_messages = []
    count_f = []
    #
    for message in messages:
        words = message.split()
        i = 0
        f_words = []
        for word in words:
            if word == "dang":
                i += 1
                word = ''
            else:
                f_words.append(word)

        f_words = " ".join(f_words)
        count_f.append(i)
        f_messages.append(f_words)

    # print(count_f)
    # print("f_words: ", f_words)
    # print("f_messages: ", f_messages)

    return f_messages, count_f


# filter_messages(
#   ["darn it", "this dang thing won't work", "lets fight one on one"])
