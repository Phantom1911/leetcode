# https://leetcode.com/playground/R2yTUsoT

obj = {
    'a': {
        'b': {
            'c': 12
        }
    }
}


def findPath(obj, path):
    path_array = path.split(".")
    return getPath(path_array, obj)

def getPath(path_array, obj):
    n = len(path_array)
    if n ==1:
        if path_array[0] not in obj :
            return None
        else:
            return obj[path_array[0]]
    if path_array[0] in obj and isinstance(obj[path_array[0]], dict):
        return getPath(path_array[1:], obj[path_array[0]])
    return None

if __name__ == "__main__":
    print(findPath(obj, 'a.b.c.d'))