def count_nested_levels(nested_documents, target_document_id, level=1):
    """ search for target id in nested document """

    if target_document_id in nested_documents:
        return 1

    for doc, nested_doc in nested_documents.items():
        # print(f'!!doc: {doc} nested_doc: {nested_doc}')

        if isinstance(nested_doc, dict):
            level = count_nested_levels(nested_doc, target_document_id)
            print(f'!level: {level}')
            if level != -1:
                return level + 1

    return -1
