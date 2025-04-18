from flet import Colors, IconButton, Icons


class SearchFiles(IconButton):
    """
    File selector component that allows users to select files from their local system.
    """

    def __init__(self, on_click: callable):

        super().__init__(
            icon=Icons.FOLDER,
            tooltip="Select a file",
            icon_size=50,
            icon_color=Colors.BLUE_500,
            on_click=on_click,
        )
