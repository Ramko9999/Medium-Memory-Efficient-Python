
def get_odds_list(n):
    odds = []
    num = 1
    for i in range(n):
        odds.append(num)
        num += 2
    return odds


def get_odds_generator(n):
    num = 1
    for i in range(n):
        yield num
        num += 2

odds = get_odds_generator(1000000)

first = next(odds)
'''
first = 1

Explanation: num is 1. We enter the for loop and immediately yield num
'''

second = next(odds)
'''
second = 3 

Explanation: num is 1. We add 2 to num, so its now 3. 
We go the next iteration of the loop and yield num
'''

third = next(odds)
'''
third = 5

Explanation: num is 3. We add 2 to num, so its now 5. 
We go to the next iteration of the loop and yield num
'''