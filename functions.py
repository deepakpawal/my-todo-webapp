def get_todos(filepath='todos.txt'):
    """Reads the todos from file and return the todos as a list"""
    with open(filepath, 'r') as file:
        todoss = file.readlines()
    return todoss


def write_todos(todoos,filepath='todos.txt'):
    """Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todoos)
    #no return because its more like a procedure


if __name__=="__main__": #when run by self then name is main but if imported by some other python file then name is 'name of this file= 'functions'
    print(get_todos())
