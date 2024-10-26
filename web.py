import streamlit as st
from streamlit import checkbox

import functions
import functions as f

def add_todo():
    todo= st.session_state["new_todo"]
    todos.append(todo+"\n")
    f.write_todos(todos)


todos = f.get_todos()

st.title("My Todo App")

st.subheader("Increase your Productivity!")

for index,todo in enumerate(todos):
    checkbox= st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="",placeholder="Add new todo",on_change=add_todo, key= "new_todo")
