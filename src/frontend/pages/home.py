import flet as ft

from src.frontend.components import Input, SearchFiles


def main(page: ft.Page):
    """
    Home page of the application.
    """
    page.title = "Home"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.window.width = 1280
    page.window.height = 720
    page.window.resizable = False
    page.window.center()

    # control vars

    data = {
        "selected_file_path": "",
        "selected_file_name": "",
    }

    file_selected_input = Input(
        label=None,
        helper_text=None,
        hint_text="select a file",
        read_only=True,
    )

    def get_selected_file_path(e: ft.FilePickerResultEvent):

        file = e.files[0] if e.files else ""
        
        if file:
            data["selected_file_path"] = file.path
            data["selected_file_name"] = file.name

        file_selected_input.set(
            data["selected_file_name"]
        )
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
            margin=ft.Margin(
                top=50,
                left=0,
                right=0,
                bottom=0,
            ),
        )
    )
