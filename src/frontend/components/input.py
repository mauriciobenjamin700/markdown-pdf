from flet import Colors, TextAlign, TextField

from src.frontend.styles import HINT_STYLE, LABEL_STYLE, TEXT_STYLE


class Input(TextField):
    """
    Input component that allows users to enter text.

    Args:
        label (str): The label for the input field.
        helper_text (str): The helper text for the input field.
        hint_text (str): The hint text for the input field.
        value (str): The initial value of the input field.
        read_only (bool): Whether the input field is read-only or not.
    """

    def __init__(
        self,
        label="Input",
        helper_text="Enter text",
        hint_text="Enter text here",
        value="",
        read_only=False,
    ):
        super().__init__(
            read_only=read_only,
            label=label,
            helper_text=helper_text,
            value=value,
            bgcolor=Colors.GREY_700,
            width=500,
            height=50,
            text_align=TextAlign.CENTER,
            align_label_with_hint=True,
            label_style=LABEL_STYLE,
            text_style=TEXT_STYLE,
            hint_text=hint_text,
            hint_style=HINT_STYLE,
        )

    def get(self):
        """
        Get the current value of the input field.

        Args:
            None

        Returns:
            str: The current value of the input field.
        """
        return self.value

    def set(self, value: str):
        """
        Set the value of the input field.

        Args:
            value (str): The new value to set for the input field.
        Returns:
            None
        """
        self.value = value
        self.update()

    def clear(self):
        """
        Clear the value of the input field.

        Args:
            None

        Returns:
            None
        """
        self.value = ""
        self.update()

    def enable(self):
        """
        Enable the input field.

        Args:
            None

        Returns:
            None
        """
        self.read_only = False
        self.update()

    def disable(self):
        """
        Disable the input field.

        Args:
            None

        Returns:
            None
        """
        self.read_only = True
        self.update()
