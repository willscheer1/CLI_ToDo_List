"""
Command Line Interface To-Do List.
The user's T-Do list is displayed in the terminal. 
The user can interact with To-Do list with the following commands:
    -add: Add's text item to the end of the To-Do list. Optional index tag (-i) can be used to specify the index where the item will be added.
        (ex. add -4 'Do the laundry')
    -del: Delete's first item from the To-Do list. Optional index tag (-i) can be used to specify the index removed.
        (ex. del -2)
    -clear: Delete's all items from the To-Do list.
    -export: Take's a file path and export's To-Do list as a .docx file. (ex. export your/path/here/my_list)
    -help: Prints list of available commands to the console.
    -exit: Exit the program.
"""
from ToDoList import ToDoList


if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.run()