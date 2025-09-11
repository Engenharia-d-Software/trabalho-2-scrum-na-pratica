import streamlit as st
import streamlit_shadcn_ui as ui
from streamlit_shadcn_ui import card as card_ui
from streamlit_card import card
import uuid



st.set_page_config(layout="wide")

def header():
    st.title('Quadro Kanban')
    st.subheader('Gerencie suas tarefas de forma visual')
    st.markdown("Gerencie suas *tarefas* de forma visual :pushpin:")


def column_title(column,title):
    with column:
        st.header(title)



def add_card(column, title, description, priority="Alta"):
    # Exemplo de card com imagem, título, texto e estilos personalizados
    with column:
        with ui.card(key=str(uuid.uuid4())):
            ui.element("span", children=[title], className="text-gray-400 text-sm font-medium m-1", key="label1")





if __name__=='__main__':
    header()

    column1, column2, column3 = st.columns(3, gap="medium", border=True)
    column_title(column1,"A Fazer")
    column_title(column2,"Em Progresso")
    column_title(column3,"Concluído")

    add_card(column1,"Tarefa 1","Fazer alguma coisa")
    add_card(column2,"Ir ao mercado","Comprar frutas, verduras e carne")
    add_card(column3,"Tarefa","ahsu shuifiosafios shuiso ahfis sihfojso so jsio")







