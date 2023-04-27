def filter_unique_dicts(list_dicts: list[dict]) -> list[dict]:
    unique_list_dicts: list = list()
    for dict_object in list_dicts:
        if dict_object not in unique_list_dicts:
            unique_list_dicts.append(dict_object)

    return unique_list_dicts


def main() -> None:
    list_dicts: list[dict[str, str]] = [
        {"key1": "value1"},
        {"k1": "v1", "k2": "v2", "k3": "v3"},
        {},
        {},
        {"key1": "value1"},
        {"key1": "value1"},
        {"key2": "value2"}
    ]
    result: list[dict[str, str]] = filter_unique_dicts(list_dicts=list_dicts)
    print(result)


if __name__ == '__main__':
    main()
