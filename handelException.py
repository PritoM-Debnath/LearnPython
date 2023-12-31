while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except :
        print("Oops!  That was no valid number.  Try again...")
    finally:
        print("Attempted Input\n")

'''try: This is the only mandatory clause in a try statement. The code in this block is the first thing that Python runs in a try statement.
except: If Python runs into an exception while running the try block, it will jump to the except block that handles that exception.
else: If Python runs into no exceptions while running the try block, it will run the code in this block after running the try block.
finally: Before Python leaves this try statement, it will run the code in this finally block under any conditions, even if it's ending the program. 
E.g., if Python ran into an error while running code in the except or else block, this finally block will still be executed before stopping the program.'''