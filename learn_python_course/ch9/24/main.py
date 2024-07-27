def filter_messages(messages):
    filtered_msgs = []
    dang_total = []

    for message in messages:
        dang_counter = 0
        filtered_words = []
        for word in message.split():
            if word == "dang":
                dang_counter += 1
            else:
                filtered_words.append(word)

        dang_total.append(dang_counter)
        filtered_msgs.append(" ".join(filtered_words))

    # print(dang_total)
    # print("filtered_words: ", filtered_words)
    # print("filtered_msgs: ", filtered_msgs)

    return filtered_msgs, dang_total


# filter_messages(
#   ["darn it", "this dang thing won't work", "lets fight one on one"])
