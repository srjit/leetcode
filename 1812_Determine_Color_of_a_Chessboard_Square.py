class Solution:

    def squareIsWhite(self, coordinates: str) -> bool:
        
        n1 = ord(coordinates[0])
        n2 = int(coordinates[1])

        return not (n1+n2) % 2 == 0
            