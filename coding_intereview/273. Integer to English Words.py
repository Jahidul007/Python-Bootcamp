class Solution:
    def numberToWords(self, num: int) -> str:

        if num == 0:
            return "Zero"

        bigs = ["", "Thousand", "Million", "Billion", "Trillion"]

        hundred = "Hundred"

        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
                "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

        def processChunk(num):

            if num == 0:
                return ""

            output = ""
            h = num // 100
            if h > 0:
                output += ones[h] + " " + hundred

            num = num % 100

            if num >= 20:
                t = num // 10
                output += " " + tens[t]
                num = num % 10

            output += " " + ones[num]

            return output.strip()

        index = 0
        result = ""
        while num:
            chunk = num % 1000
            chunk = processChunk(chunk)
            if chunk:
                result = chunk + " " + bigs[index] + " " + result

            num = num // 1000
            index += 1

        return result.strip()