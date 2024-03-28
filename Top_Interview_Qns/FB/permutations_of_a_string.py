

def permute(s):

    if len(s) == 1:
        return s

    result = []
    for i, v in enumerate(s):
        result += [v + p for p in permute(s[:i] + s[i+1:])]

    return result 


print(permute("abc"))