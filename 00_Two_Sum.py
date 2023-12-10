
def two_sum(input: list[int], target: int) -> list[int]:

    d = {i: idx for idx, i in enumerate(input)}

    for idx, i in enumerate(input):
        partner = target - i
        if partner in d and partner != i:
            return [idx, d[partner]]
            
    return [-1,-1]

print(f"Indices are : {two_sum([2,3,4,5,6,9], 11)}")