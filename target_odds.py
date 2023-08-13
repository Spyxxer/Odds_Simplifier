#This function is here to handle errors incase a wrong value is inserted.
import copy
import random
def get_odd():
        odd = None
        try:
            odd = float(input("Enter an Odd :"))
        except:
            print("Wrong Value")
            get_odd() #Recursion occurs here...
        else:
            odds.append(odd)

def multiply(arr):
    n = 1
    for e in arr:
        n *= e
    return n

def find_comb(odds_arr, target, no_of_options, i=0):
    if i >= no_of_options:
        return
    else:  
        add = []; mul = 1
        odds_copy = copy.deepcopy(odds_arr) #Creates a deep copy of the original object..
        keys = list(odds_copy)
        while mul <= target and keys:
            get_val = random.choice(keys)
            if odds_copy[get_val] > 0:
                add.append(get_val); odds_copy[get_val] -= 1
                mul *= get_val
            else:
                keys.remove(get_val)
    print(add, 'total = ', mul)
    find_comb(odds_arr, target, no_of_options, i+1)

odds = []
no_of_games = int(input("Enter number of games : "))
i = 0
while i < no_of_games:
    get_odd(); i += 1

odds_dict = {}
for each in odds:
    if each not in odds_dict:
        odds_dict[each] = 1
    else:
        odds_dict[each] += 1
dup = odds_dict
print("Odds generated :", odds)
print("Listed accordingly -->", odds_dict)

target_odd = float(input("Enter target no of odds : "))
while target_odd > multiply(odds):
    target_odd = float(input("Enter target no of odds : "))
options = int(input("Enter number of possible choices : "))

find_comb(odds_dict, target_odd, options)





