def deduplicate_lists(lst1, lst2, reverse=False):
    if reverse:
        return sorted(list(set((lst1 + lst2))), reverse=True)
    else:
        return sorted(list(set((lst1 + lst2))))

    # return sorted(set(lst1 + lst2), reverse=reverse)
