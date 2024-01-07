'''Write a function called generate_password that selects three random words from the list of words word_list and concatenates them into a single string. 
Your function should not accept any arguments and should reference the global variable word_list to build the password. 
To help with this, check out the choice function associated with the random module in the Standard Library.'''

import random

word_file = "file.txt"
word_list = []

with open(word_file,'r') as words:
    for line in words:
        # remove white space and make everything lowercase
        word = line.strip().lower()
        if 3 < len(word) < 8:
            word_list.append(word)

def generate_password():
    return "{}{}{}".format(word_list[random.randint(0, len(word_list))],word_list[random.randint(0, len(word_list))],word_list[random.randint(0, len(word_list))])
    #return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)
    #return ''.join(random.sample(word_list, 3))


password = generate_password()

print(password)