from math import ceil


def split_list(items: list) -> list:
    return [items[0:ceil(len(items) / 2)], items[ceil(len(items) / 2):]]


if __name__ == '__main__':
    print(split_list([1, 2, 3]))
