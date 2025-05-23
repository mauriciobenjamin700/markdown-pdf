from os import mkdir
from os.path import abspath, basename, exists, join

import flet as ft

from src.backend import markdown_to_pdf
from src.frontend.components import Alert, ConvertDoc, Input, SearchFiles


def setup_page(page: ft.Page):
    """
    Base setup for the page.
    """
    page.title = "Home"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.width = 1280
    page.window.height = 720
    page.window.resizable = False
    page.window.center()


def initialize_data():
    """
    initialize data for the application.
    """
    data = {
        "selected_file_path": "",
        "selected_file_name": "",
        "output_path": abspath("pdf/"),
        "output_file_name": "",
    }

    if not exists(data["output_path"]):
        mkdir(data["output_path"])

    return data


def create_alerts(page, data):
    """
    Create alerts for the application.
    """

    def handle_close_alert(e):
        for value in alerts.values():
            if value.open:
                page.close(value)

    alerts = {
        "error": Alert(
            title="Error",
            content="Please select a markdown file",
            on_click=handle_close_alert,
        ),
        "success": Alert(
            title="Success",
            content=f"File converted to {data['output_file_name']}.pdf and saved to {abspath(data['output_path'])}",
            on_click=handle_close_alert,
        ),
    }

    return alerts


def handle_convert(page, data, alerts, output):
    """
    Handle the convert button click event.
    """

    def convert(e=None):
        data["output_file_name"] = (
            output.get() if output.get() else data["output_file_name"]
        )

        if data["selected_file_path"]:
            md_file = data["selected_file_path"]
            ext = basename(md_file).split(".")[-1]
            if ext not in ["md", "MD"]:
                page.open(alerts["error"])
            else:
                if data["output_file_name"] == "":
                    data["output_file_name"] = basename(md_file).split(".")[0]

                markdown_to_pdf(
                    data["selected_file_path"],
                    join(data["output_path"], data["output_file_name"] + ".pdf"),
                )

                page.open(alerts["success"])
        else:
            page.open(alerts["error"])

    return convert


def main(page: ft.Page):
    """
    Home page of the application.
    """
    setup_page(page)
    data = initialize_data()
    alerts = create_alerts(page, data)

    file_selected_input = Input(
        label=None,
        helper_text=None,
        hint_text="select a file",
        read_only=True,
    )

    output = Input(
        label=None,
        helper_text=None,
        hint_text="output path",
        read_only=False,
    )

    def get_selected_file_path(e: ft.FilePickerResultEvent):
        file = e.files[0] if e.files else ""

        if file:
            data["selected_file_path"] = file.path
            data["selected_file_name"] = file.name

        file_selected_input.set(data["selected_file_name"])
        file_selected_input.update()

    pick_files_dialog = ft.FilePicker(on_result=get_selected_file_path)
    page.overlay.append(pick_files_dialog)

    page.add(
        ft.Container(
            content=ft.Row(
                [
                    file_selected_input,
                    SearchFiles(lambda _: pick_files_dialog.pick_files()),
                    pick_files_dialog,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            margin=ft.Margin(top=50, left=0, right=0, bottom=0),
        )
    )

    page.add(
        ft.Container(
            content=ft.Row(
                [
                    output,
                    ConvertDoc(on_click=handle_convert(page, data, alerts, output)),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            margin=ft.Margin(top=50, left=0, right=0, bottom=0),
        )
    )
