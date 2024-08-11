def index_keywords(document, index):
    d = index.copy()
    if document in d:
        return d[document], d
    found_keywords = find_keywords(document)
    d[document] = found_keywords
    return found_keywords, d


def find_keywords(document):
    """ find keyword in document """
    keywords = [
        "functional",
        "immutable",
        "declarative",
        "higher-order",
        "lambda",
        "deterministic",
        "side-effects",
        "memoization",
        "referential transparency",
    ]

    return list(filter(lambda keyword: keyword in document, keywords))
