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