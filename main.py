"""
Command Line Interface To-Do List.
The user's T-Do list is displayed in the terminal. 
The user can interact with To-Do list with the following commands:
    -add: Add's text item to the end of the To-Do list. Optional index tag (-i) can be used to specify the index where the item will be added.
        (ex. add -4 'Do the laundry')
    -remove: Remove's last entered text item from the To-Do list. Option index tag (-i) can be used to specify the index removed.
        (ex. remove -2)
    -clear: Remove's every item from the To-Do list.
    -export: Take's a string value as a file name and export's To-Do list as a .docx file.
"""
from ToDoList import ToDoList


if __name__ == "__main__":
    pass