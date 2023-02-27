def join(*params, sep = '-'):
    if not params:
        return None
    L = []
    for i in range(len(params)):
        try:
            iter(params[i])
        except:
            raise TypeError(params[i], 'is not iterable')
        for j in range(len(params[i])):
            L.append(params[i][j])
        L.append(sep)
    del L[-1]
    return L
print(join([1, 2], [8], [9, 5, 6], sep = '@'))
print(join([1, 2], [8], [9, 5, 6]))
print(join([1]))
print(join())