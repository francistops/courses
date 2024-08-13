def sum_nested_list(lst):
    size = 0
    print("!i'm here")
    for dir in lst:
        if isinstance(dir, int):
            print(f'!size before add: {size}')
            size += dir
            print(f'!size after add: {size}')
        elif isinstance(dir, list):
            print(f'before recursion: {size}')
            size += sum_nested_list(dir)
    print(f'!final: {size}')
    return size
