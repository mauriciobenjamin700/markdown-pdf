import flet as ft

from src.frontend.components import Input


def main(page: ft.Page):
    """
    Home page of the application.
    """
    page.title = "Home"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.add(
        ft.Row(
            [
                Input(
                    label="File selected",
                    helper_text="",
                    read_only=False,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
            wrap=True,
        )
    )