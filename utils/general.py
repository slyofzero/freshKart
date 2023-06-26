def flatten_dict_values(values):
    flat = tuple(map(lambda item: item[0], values))

    return flat
