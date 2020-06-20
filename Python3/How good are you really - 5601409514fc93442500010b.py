# [8 kyu] How good are you really?
# Language: Python
# Kata: https://www.codewars.com/kata/5601409514fc93442500010b
# My CodeWars profile: https://www.codewars.com/users/Thundiverter

# Solution
def better_than_average(class_points, your_points):
    return bool(your_points > (sum(class_points)/len(class_points)))
