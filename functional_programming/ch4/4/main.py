
def zipmap(keys, values):
    if not keys or not values:
        return {}

    first_key = keys[0]
    first_value = values[0]
    rest_keys = keys[1:]
    rest_values = values[1:]

    return {first_key: first_value, **zipmap(rest_keys, rest_values)}
