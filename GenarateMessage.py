def get_list_from_user_input(prompt):
    """Get a list of items from user input, separated by commas."""
    user_input = input(prompt)
    return [item for item in user_input.title().split(',')]

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \ submit before you can graduate. Your current grade is {} and can increase \ to {} if you submit all assignments before the due date.\n\n"

names =  get_list_from_user_input("Enter names separated by commas: ") 
assignments =  get_list_from_user_input("Enter assignment counts separated by commas: ")
grades =  get_list_from_user_input("Enter grades separated by commas: ")

for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment) * 2))
