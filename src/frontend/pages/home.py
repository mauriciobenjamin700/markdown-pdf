import flet as ft

from src.frontend.components import Input


def main(page: ft.Page):
    """
    Home page of the application.
    """
    page.title = "Home"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.add(
        ft.Container(
            content=ft.Row(
                [
                    Input(
                        label=None,
                        helper_text=None,
                        hint_text="select a file",
                        read_only=True,
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            margin=ft.Margin(
                top=50,
                left=0,
                right=0,
                bottom=0,
            )
        )
    )