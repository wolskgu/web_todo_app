import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    new_todo = st.session_state["new_todo"].strip() + "\n"
    if new_todo:
        todos.append(new_todo.title())
        functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My To-Do App")
st.subheader("Keep your life organized!")
# st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a To-Do:", placeholder="Add a new To-Do",
              on_change=add_todo, key="new_todo")



