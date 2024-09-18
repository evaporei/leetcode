class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        digits[-1] += 1
        for i in range(len(digits) - 1, -1, -1):
            newVal = digits[i] + carry
            if newVal >= 10:
                digits[i] = newVal % 10
                carry = 1
            else:
                digits[i] = newVal
                carry = 0
        if carry:
            digits.insert(0, carry)

        return digits
