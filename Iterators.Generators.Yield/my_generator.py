import hashlib


def hash_file(path: str):
    with open(path, 'rb') as file:
        for string in file:
            hash_obj = hashlib.md5(string)
            yield hash_obj.hexdigest()
