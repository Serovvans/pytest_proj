def get_val(collection, key, default=None):
    """
    Функция возвращает значение из словаря по переданному ключу, если ключ существует.
    В ином случае возвращается значение default
    :param collection: словарь, элемент которого нуджно получить
    :param key: ключ искомого элемента
    :param default: значение, которое возвращает функция, если ключа в словаре нет
    :return: искомый элемент или значение по умолчанию
    """
    if key not in collection:
        return default

    return collection[key]
