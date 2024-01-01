
from itertools import groupby

class Solution:

    def generate_tuples(self, input_str):
        return [(char, len(list(group))) for char, group in groupby(input_str)]


    def get_combinations(self, target, distinct):

        if distinct == 3:

            arr = [1,1,2]
            if target < 3:
                return arr[target]
            else:
                for i in range(3, target+1):
                    arr.append(arr[i-1] + arr[i-2] + arr[i-3])
                return arr[target]

        else:

            arr = [1,2,4,8]
            if target <= 4:
                return arr[target-1]
            else:
                for i in range(4, target+1):
                    arr.append(arr[i-1] + arr[i-2] + arr[i-3]  + arr[i-4])
                return arr[target-1]
            

    def countTexts(self, pressedKeys: str) -> int:

        _keymap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        _d = self.generate_tuples(pressedKeys) 
        
        res = 1
        for key, target in _d:
            distinct_alphabets = len(_keymap[key])
            combinations = self.get_combinations(target, distinct_alphabets)
            res *= combinations

        return res % (10**9 + 7)
            

        

