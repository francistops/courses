def restore_documents(originals, backups):
    return set(
        filter(
            lambda doc: not doc.isdigit(),
            map(str.upper, originals + backups)))
