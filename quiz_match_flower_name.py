'''Create a function that opens the flowers.txt, reads every line in it, and saves it as a dictionary. The main (separate) function should take 
user input (user's first name and last name) and parse the user input to identify the first letter of the first name. It should then use it to print 
the flower name with the same first letter (from dictionary created in the first function).'''
# Write your code here
def read_flower_name(file_path):
    flower_dict = {}
    with open('flowers.txt', 'r') as f:
        for l in f:
            name, flower = l.strip().split(':')
            flower_dict[name] = flower
    return flower_dict
# HINT: create a dictionary from flowers.txt
def flower_name(dic, name):
    flag = name[0].upper()
    if flag in dic:
        return dic[flag]
    else :
        return "No flower found for the given initial."
# HINT: create a function to ask for user's first and last name

def main():
    file_path = 'flowers.txt'
    flower_dict = read_flower_name(file_path)
    
    user_first_name = input("Enter your first name: ")
    user_last_name = input("Enter your last name: ")
    
    flower = flower_name(flower_dict, user_first_name)
    if flower:
        print(f"Dear {user_first_name} {user_last_name}, your flower is: {flower}")
    else:
        print("No flower found for the given input.")
# print the desired output

if __name__ == "__main__":
    main()