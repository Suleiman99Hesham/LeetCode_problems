class Solution:
    def intToRoman(self, num: int) -> str:
        subtractions = {
            4: 'IV',
            9: 'IX',
            40: 'XL',
            90: 'XC',
            400: 'CD',
            900: 'CM',
        }
        romans = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M',
        }
        mul = 1
        result = ""
        while num > 0:
            digit = (num % 10)
            found = subtractions.get((digit * mul), None)
            if not found:
                part = ''
                for key in sorted(romans.keys(), reverse=True):
                    rem = (digit * mul) % key
                    if rem < (digit * mul):
                        part += (romans[key] * digit) if rem == 0 and (digit * mul) != key else romans[key]
                        digit %= (key // mul)
                        if digit == 0:
                            break
                result = part +result
            else:
                result = found + result
            num //= 10
            mul *= 10
        return result