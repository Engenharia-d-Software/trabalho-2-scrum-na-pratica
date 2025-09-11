import streamlit as st
import streamlit_shadcn_ui as ui

st.title('Quadro Kanban')
st.subheader('Gerencie suas tarefas de forma visual')
st.markdown("Gerencie suas *tarefas* de forma visual :pushpin:")

#collumns of kanban
column1, column2, column3 = st.columns(3,gap="medium",border=True)

with column1:
    st.header('A Fazer')
    x = st.slider('x')
    st.write(x, 'squared is', x * x)

with column2:
    st.header('Em Progresso')

with column3:
    st.header('Concluído')

