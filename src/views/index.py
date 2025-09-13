import uuid
import streamlit as st
from streamlit_card import card
from streamlit_shadcn_ui import card as card_ui
import streamlit_shadcn_ui as ui

from control import task_step
import model
import schemas

st.set_page_config(layout="wide")


def header():
    st.title("Quadro Kanban")
    st.subheader("Gerencie suas tarefas de forma visual")
    st.markdown("Gerencie suas *tarefas* de forma visual :pushpin:")


def column_title(column, title):
    with column:
        st.header(title)


def add_card(column, issue: model.Issue):
    # Exemplo de card com imagem, título, texto e estilos personalizados
    with column:
        with ui.card(key=str(uuid.uuid4())):
            ui.element(
                "span",
                children=[issue.title],
                className="text-gray-400 text-sm font-medium m-1",
                key="label1",
            )


if __name__ == "__main__":
    header()

    DEFAULT_COLUMN_NAMES = ["A Fazer", "Em Progresso", "Concluido"]
    ui_columns = st.columns(len(DEFAULT_COLUMN_NAMES), gap="medium", border=True)
    for column, column_widget in zip(DEFAULT_COLUMN_NAMES, ui_columns):
        db_task_step = task_step.ensure_created(schemas.TaskStepCreate(name=column))
        column_title(column_widget, column)
        for issue in db_task_step.issues:
            add_card(column_widget, issue)
