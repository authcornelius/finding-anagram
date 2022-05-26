# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams():
    # [assignment] Add your code here
    

    firstString = input("Enter First Word \n").lower()
    secondString = input("Enter Second Word \n").lower()

    str1 = sorted(firstString)
    str2 = sorted(secondString)

    if str1 == str2:
        print('True')
    else:
        print('False')

find_anagrams()

