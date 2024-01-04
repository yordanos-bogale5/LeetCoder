class Solution:
    def smallestEvenMultiple(self, n):
        multiple = n

        while True:
            if multiple % 2 == 0 and multiple % n == 0:
                return multiple
            multiple += n

