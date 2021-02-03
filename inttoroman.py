class Solution(object):
    def intToRoman(self, num):
        v = [1000, 100, 10, 1]
        s = ["M", "C", "X", "I"]
        h = ["",  "D", "L", "V" ]
        res = ""
        for i in range(len(v)):
            if not num:
                break
            times = num // v[i]
            num %= v[i]
            if times < 4:
                res += s[i] * times
            elif times == 4:
                res += s[i] + h[i]                     
            elif times < 9:
                res += h[i] + s[i] * (times - 5)
            else:
                res += s[i] + s[i - 1]                    
        return res
