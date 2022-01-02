class Solution:
    def romanToInt(self, s: str) -> int:
        listStr = list(s)
        counter = 0
        answer = 0
        while len(listStr) > counter:
            if listStr[counter] == 'I':
                if counter != len(listStr):
                    if listStr[counter + 1] == 'V':
                        answer += 4
                        counter += 2
                        break
                    elif listStr[counter + 1] == 'X':
                        answer += 10
                        counter += 2
                        break
                    else:
                        answer += 1
                        break
                else:
                    answer += 1
            elif listStr[counter] == 'V':
                answer += 5
            elif listStr[counter] == 'X':
                if counter != len(listStr):
                    if listStr[counter + 1] == 'L':
                        answer += 40
                        counter += 2
                        break
                    elif listStr[counter + 1] == 'C':
                        answer += 90
                        counter += 2
                        break
                    else:
                        answer += 10
                        break
                else:
                    answer += 10
            elif listStr[counter] == 'L':
                answer += 50
            elif listStr[counter] == 'C':
                if counter != len(listStr):
                    if listStr[counter + 1] == 'D':
                        answer += 400
                        counter += 2
                        break
                    elif listStr[counter + 1] == 'M':
                        answer += 900
                        counter += 2
                        break
                    else:
                        answer += 100
                        break
                else:
                    answer += 100
            elif listStr[counter] == 'D':
                answer += 500
            elif listStr[counter] == 'M':
                answer += 1000
            counter += 1
        return answer

# solution = Solution()
# s = input()
# print(solution.romanToInt(s))


class Solution:
# @param {string} s
# @return {integer}
    def romanToInt(self, s):
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        z = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]
        return z + roman[s[-1]]