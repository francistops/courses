def list_files(current_filetree, current_path=""):
    """ take dict, str """
    file_paths = []

    for node, nested_nodes in current_filetree.items():
        new_path = f'{current_path}/{node}'
        print(f'!{current_path}/{node}')

        if nested_nodes is None:
            file_paths.append(new_path)

        else:
            file_paths.extend(list_files(nested_nodes, new_path))

    return file_paths
