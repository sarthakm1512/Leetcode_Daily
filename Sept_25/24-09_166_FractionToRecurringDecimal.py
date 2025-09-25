#Question Link: https://leetcode.com/problems/fraction-to-recurring-decimal/?envType=daily-question&envId=2025-09-24
"""
166. Fraction to Recurring Decimal

Problem Statement: Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
If the fractional part is repeating, enclose the repeating part in parentheses.
If multiple answers are possible, return any of them.
It is guaranteed that the length of the answer string is less than 10^4 for all the given inputs.

Example 1:
Input: numerator = 1, denominator = 2
Output: "0.5"

Example 2:
Input: numerator = 2, denominator = 1
Output: "2"

Example 3:
Input: numerator = 4, denominator = 333
Output: "0.(012)"
 
Constraints:
-2^31 <= numerator, denominator <= 2^31 - 1
denominator != 0
"""

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        #Step 1: Handle Negative result
        if numerator == 0:
            return "0"
        result = []
        if (numerator < 0) ^ (denominator < 0): #XOR for opposite signs
            result.append("-")

        #Step 2: Work with absolute values
        numerator, denominator = abs(numerator), abs(denominator)

        #Step 3: Integer part
        integer_part = numerator // denominator
        result.append(str(integer_part))

        remainder = numerator % denominator
        if remainder == 0:
            return "".join(result) #No decimal part
        result.append(".") #Start decimal part

        #Step 4: Decimal part with remainder tracking
        remainder_map = {}
        while remainder != 0:
            if remainder in remainder_map:
                #Repeating remainder found
                idx = remainder_map[remainder]
                result.insert(idx, "(")
                result.append(")")
                break
            
            remainder_map[remainder] = len(result)

            remainder *= 10
            result.append(str(remainder//denominator))
            remainder %= denominator
        
        return "".join(result)
