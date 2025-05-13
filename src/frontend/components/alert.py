from flet import AlertDialog, Text, TextButton


class Alert(AlertDialog):
    def __init__(
        self,
        title: str,
        content: str,
        on_click: callable = None,
    ):
        super().__init__(
            title=Text(title),
            content=Text(content),
            actions=[
                TextButton(
                    "OK",
                    on_click=on_click,
                )
            ],
        )
