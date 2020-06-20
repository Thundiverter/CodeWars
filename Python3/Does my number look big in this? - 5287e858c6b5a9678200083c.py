# [6 kyu] Does my number look big in this?
# Language: Python
# Kata: https://www.codewars.com/kata/5287e858c6b5a9678200083c/train/python
# My CodeWars profile: https://www.codewars.com/users/Thundiverter

# Solution
def narcissistic(value):
    res = 0
    for i in range(len(str(value))):
        res += int(str(value)[i]) ** len(str(value))
    if value == res:
        return True
    else:
        return False
