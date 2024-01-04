class Solution:
    def selfDividingNumbers(self, left, right):
        result = []

        for num in range(left, right + 1):
            if '0' not in str(num):
                is_self_dividing = True
                for digit in str(num):
                    if num % int(digit) != 0:
                        is_self_dividing = False
                        break
                if is_self_dividing:
                    result.append(num)

        return result
