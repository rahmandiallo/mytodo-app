import streamlit as st
import functions

todos = functions.get_todos()

st.set_page_config(layout="wide")

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This my todo app!")
st.write("<h1>This app is to increase your <b>productivity!</b>.</h1>",unsafe_allow_html=True)

st.text_input(label = "Enter A Todo:",placeholder = "Add New Todo",on_change = add_todo, key = "new_todo")


for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

print("Hello")
